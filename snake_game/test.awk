BEGIN {
    current_time = ""
    drop_threshold_warn = 0.1
    drop_threshold_crit = 1
    drop_level = "OK"
    drop_event_file = "/tmp/port_drop_events.log"

    # 이전 데이터 읽기
    prev_txpacket = 0
    prev_txdrop = 0
    if ((getline prev_line < "/tmp/port_stats_prev.dat") > 0) {
        split(prev_line, prev_data, ",")
        prev_txpacket = prev_data[1]
        prev_txdrop = prev_data[2]
    }
    close("/tmp/port_stats_prev.dat")

    printf "%17s %8s %8s %8s %8s %8s %8s %8s %8s\n",
           "Date-Time", "UpTxP", "UpTxMB", "DnRxP", "DnRxMb", "UpTxPD", "UpDrD", "UpDrR", "DrLvl"
    printf "%17s %8s %8s %8s %8s %8s %8s %8s %8s\n", "----------------", "--------", "--------", "--------", "--------", "--------", "--------", "--------", "--------"
}

# 시간 정보 추출
/^Time:/ {
    current_time = $2 " " $3
    dn_rx_pps = 0
    dn_rx_bps = 0
    in_monitoring = 0
    in_statistics = 0
}

# 포트 모니터링 시작
/show port-monitoring/ {
    in_monitoring = 1
    next
}

# 포트 모니터링 헤더 제거
in_monitoring && (/Port Monitoring Table|Port.*RxRate.*TxRate|^-+/) {
    next
}

# 포트 모니터링 데이터 추출
in_monitoring && /^[0-9]+[ \t]*\|/ {
    gsub(/^ +| +$/, "")
    split($0, fields, /[ \t]*\|[ \t]*/)
    port = fields[1]
    rx_pps = fields[2]
    rx_bps = fields[3]
    tx_pps = fields[4]
    tx_bps = fields[5]

    if (port == 1) {
        up_tx_pps = tx_pps
        up_tx_bps = tx_bps
    } else if (port >= 2 && port <= 24) {
        dn_rx_pps += rx_pps
        dn_rx_bps += rx_bps
    }
}

# 통계 섹션 시작
/show port statistics/ {
    in_statistics = 1
    in_monitoring = 0
    next
}

# 헤더 무시
in_statistics && (/Interface.*TX|face.*bytes.*packets|^-+/) {
    next
}

# Port 1의 통계 추출
in_statistics && /^ *1 *\|/ {
    split($0, sections, "|")
    tx_section = sections[3]
    gsub(/^ +| +$/, "", tx_section)
    split(tx_section, tx_fields, / +/)

    current_txpacket = tx_fields[2]
    current_txdrop = tx_fields[4]
}

# 종료 조건
in_statistics && /^K2-SFU/ {
    in_statistics = 0
    print_results()
}

# 결과 출력 함수
function print_results() {
    txpacket_delta = current_txpacket - prev_txpacket
    txdrop_delta = current_txdrop - prev_txdrop
    drop_rate = (txpacket_delta > 0) ? (txdrop_delta / txpacket_delta) * 100 : 0

    if (drop_rate > drop_threshold_crit)
        drop_level = "CRIT"
    else if (drop_rate > drop_threshold_warn)
        drop_level = "WARN"
    else
        drop_level = "OK"

    print current_txpacket "," current_txdrop > "/tmp/port_stats_prev.dat"
    close("/tmp/port_stats_prev.dat")

    res = sprintf("%17s %8d %8.2f %8d %8.2f %8d %8d %8.2f %8s",
                  current_time,
                  up_tx_pps, up_tx_bps / 1000000,
                  dn_rx_pps, dn_rx_bps / 1000000,
                  txpacket_delta, txdrop_delta,
                  drop_rate, drop_level)
    print res
    if (drop_level != "OK") {
        print res >> drop_event_file
        close(drop_event_file)
    }

    prev_txpacket = current_txpacket
    prev_txdrop = current_txdrop
}
