#!/bin/bash

gawk 'match($0, /ia-na "(([^"\\]|\\.)*)"/, m) { print m[1] }' /var/lib/dhcpd/dhcpd6.leases \
gawk 'match($0, /ia-na "(([^"\\]|\\.)*)"/, m) { print m[1] }' /var/lib/dhcpd/dhcpd6.leases \
| while IFS= read -r s; do
  hex=$(printf '%b' "$s" | xxd -p -c 1000)
  bytes=$((${#hex} / 2))
  ((bytes >= 8)) || { echo "skip: too short ($bytes B) hex=$hex"; echo "---"; continue; }

  iaid=${hex:0:8}
  duid_type=${hex:8:4}
  printf 'IAID=0x%s (%d)\n' "$iaid" "$((16#iaid))"

  case "$duid_type" in
    0001)
      ((bytes >= 12)) || { echo "bad LLT: too short"; echo "---"; continue; }
      htype=${hex:12:4}
      time_hex=${hex:16:8}
      link_off_bytes=12
      link_len_bytes=$(( bytes - link_off_bytes ))
      mac_hex=${hex:$(($link_off_bytes)):$(($link_len_bytes * 2))}
      mac=$(printf '%s' "$mac_hex" | sed 's/../&:/g; s/:$//')
      printf 'DUID-LLT (0001) HTYPE=0x%s\n' "$htype"
      printf '  TIME=0x%s (%d sec since 2000-01-01)\n' "$time_hex" "$((16#time_hex))"
      epoch=$((946684800 + 16#$time_hex))
      date -ud "@$epoch" 2>/dev/null || date -r "$epoch" ## date -ud "@초" → 해당 초(epoch time)를 UTC 날짜/시간으로 변환
      printf 'L2ADDR=%s\n' "$mac"
      ;;
    0002) duid_type_str="DUID-EN" ;;

    0003) duid_type_str="DUID-LL" ;;
      (()bytes >=8)) || { echo "bad LL: too short"; echo "---"; continue; }
      htype=${hex:12:4}
      link_off_bytes=8
      link_len_bytes=$(( bytes - link_off_bytes ))
      mac_hex=${hex:$(($link_off_bytes)):$(($link_len_bytes * 2))}
      mac=$(printf '%s' "$mac_hex" | sed 's/../&:/g; s/:$//')
      printf 'DUID-LL (0003) HTYPE=0x%s\n' "$htype"
      printf 'L2ADDR=%s\n' "$mac"
      ;;
    0004) duid_type_str="DUID-UUID" ;;
    *) duid_type_str="Unknown DUID type (0x$duid_type)"
      printf 'Go away~ duid_type is not supported: 0x%s\n' "$duid_type"
      ;;
  esac
  echo "---"
done