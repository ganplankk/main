from collections import Counter

def transform_filter_data(filter_data, port_data, log_mode="enable"):
    output_lines = ["security"]
    output_lines = ["  firewall"]
    filters = []
    filter_group_accept = []
    filter_group_drop = []

    # Well-known port dictionary
    port_map = {
        "dns": 53,
        "ntp": 123,
        "ssh": 22,
        "ftp": 21,
        "http": 80,
        "https": 443,
        "smtp": 25,
        "pop3": 110,
        "imap": 143,
        "snmp": 161,
        "ldap": 389,
        "rdp": 3389
    }

    # Collect warnings
    vlan_warnings = []
    port_warnings = []
    add_warnings = []

    # Parse port data to collect all active filters
    # port_filters 리스트에 1~2024 숫자를 넣음
    port_filters = set()
    for block in port_data.strip().split("/c/slb/port"):
        if not block.strip():
            continue
        lines = block.strip().split("\n")
        for line in lines:
            if "add" in line:
                add_values = line.split()[-1]
                # Extract range values (e.g., 10-12)
                if "-" in add_values:
                    start, end = map(int, add_values.split("-"))
                    port_filters.update(range(start, end + 1))
                else:
                    port_filters.add(int(add_values))

    # Parse filter data
    filt_data = []
    all_add_values = []

    for block in filter_data.strip().split("/c/slb/filt"):
        if not block.strip():
            continue
        lines = block.strip().split("\n")
        filt_id = lines[0].strip()
        action_line = next((line for line in lines if "action" in line), None)
        action = "accept" if "allow" in action_line else "drop"

        proto_line = next((line for line in lines if "proto" in line), None)
        protocol = proto_line.split()[-1] if proto_line else "all"

        sip_line = next((line for line in lines if "sip" in line), None)
        source_ip = sip_line.split()[-1]

        smask_line = next((line for line in lines if "smask" in line), None)
        source_mask = smask_line.split()[-1]

        dip_line = next((line for line in lines if "dip" in line), None)
        dest_ip = dip_line.split()[-1]

        dmask_line = next((line for line in lines if "dmask" in line), None)
        dest_mask = dmask_line.split()[-1]

        vlan_line = next((line for line in lines if "vlan" in line), None)
        vlan_value = vlan_line.split()[-1] if vlan_line else "any"

        # Collect add values
        add_lines = [line for line in lines if "add" in line]
        add_values = [line.split()[-1] for line in add_lines]

        if not add_lines:
            if int(filt_id) not in port_filters:
                add_warnings.append(f"filt {filt_id}가 적용된 Port는 없습니다.")
        else:
            all_add_values.append(" ".join(add_values))

        # Convert IP and mask to CIDR format
        source_cidr = "0.0.0.0/0" if source_ip == "any" else f"{source_ip}/{sum(bin(int(x)).count('1') for x in source_mask.split('.'))}"
        dest_cidr = "0.0.0.0/0" if dest_ip == "any" else f"{dest_ip}/{sum(bin(int(x)).count('1') for x in dest_mask.split('.'))}"

        sport_line = next((line for line in lines if "sport" in line), None)
        dport_line = next((line for line in lines if "dport" in line), None)

        source_port = "any"
        dest_port = "any"

        # Check for well-known ports (only alphabetic port names)
        if sport_line:
            sport = sport_line.split()[-1]
            if not sport.isdigit() and sport not in port_map:
                port_warnings.append(f"filt {filt_id}의 sport가 {sport}입니다.")
            source_port = f"eq port-num {port_map.get(sport, sport)}"

        if dport_line:
            dport = dport_line.split()[-1]
            if not dport.isdigit() and dport not in port_map:
                port_warnings.append(f"filt {filt_id}의 dport가 {dport}입니다.")
            dest_port = f"eq port-num {port_map.get(dport, dport)}"

        # Conditionally add source-port and dest-port for tcp and udp protocols
        include_source_port = not sport_line and protocol in ["tcp", "udp"]
        include_dest_port = not dport_line and protocol in ["tcp", "udp"]

        # Add vlan warning if it's not "any"
        if vlan_value != "any":
            vlan_warnings.append(f"filt {filt_id}의 vlan이 {vlan_value}입니다.")

        # Store filter data
        filt_data.append({
            "filt_id": filt_id,
            "protocol": protocol,
            "source_cidr": source_cidr,
            "dest_cidr": dest_cidr,
            "source_port": source_port,
            "dest_port": dest_port,
            "action": action,
            "include_source_port": include_source_port,
            "include_dest_port": include_dest_port,
            "vlan_value": vlan_value,
            "add_values": add_values
        })

        # Add filter to appropriate group
        if action == "accept":
            filter_group_accept.append(f"f{filt_id}")
        else:
            filter_group_drop.append(f"f{filt_id}")

    # Determine the most common add values
    if all_add_values:
        most_common_add_values = Counter(all_add_values).most_common(1)[0][0]

        # Generate warnings for add values that differ from the most common
        for filt in filt_data:
            current_add_values = " ".join(filt["add_values"])
            if current_add_values and current_add_values != most_common_add_values:
                add_warnings.append(f"filt {filt['filt_id']}의 add는 {current_add_values}입니다.")

    # Generate filters
    for filt in filt_data:
        filters.append(f"    filter f{filt['filt_id']}")
        filters.append(f"      protocol {filt['protocol']}")
        filters.append(f"      source-ip {filt['source_cidr']}")
        filters.append(f"      dest-ip {filt['dest_cidr']}")
        filters.append(f"      log {log_mode}")
        filters.append(f"      action {filt['action']}")
        if filt["include_dest_port"] or filt["dest_port"] != "any":
            filters.append(f"      dest-port {filt['dest_port']}")
        if filt["include_source_port"] or filt["source_port"] != "any":
            filters.append(f"      source-port {filt['source_port']}")
        filters.append("      apply")
        filters.append("")

    output_lines.extend(filters)
    output_lines.append("    apply")

    # Filter group for drop actions
    if filter_group_drop:
        output_lines.append("    filter-group drop")
        output_lines.append(f"      filter {','.join(filter_group_drop)}")
        output_lines.append("      apply")

    # Filter group for accept actions
    if filter_group_accept:
        output_lines.append("    filter-group accept")
        output_lines.append(f"      filter {','.join(filter_group_accept)}")
        output_lines.append("      apply")

    output_lines.append("    exit")
    output_lines.append("    exit")

    # Add warnings to the output
    if vlan_warnings:
        output_lines.append("\n".join(vlan_warnings))
    if port_warnings:
        output_lines.append("\n".join(port_warnings))
    if add_warnings:
        output_lines.append("\n".join(add_warnings))

    return "\n".join(output_lines)


# Example input data for testing
port_data_input = """
/c/slb/port "1"
        client ena
        server ena
/c/slb/port "2"
        client ena
        server ena
/c/slb/port "3"
        client ena
        server ena
        filt ena
        add 1-11
        add 14-44
        add 46-135
        add 2048
/c/slb/port "4"
        client ena
        server ena
/c/slb/port "5"
        client ena
        server ena
/c/slb/port "6"
        client ena
        server ena
/c/slb/port "7"
        client ena
        server ena
/c/slb/port "8"
        client ena
        server ena
/c/slb/port "9"
        client ena
        server ena
/c/slb/port "10"
        client ena
        server ena
/c/slb/port "11"
        client ena
        server ena
/c/slb/port "12"
        client ena
        server ena
/c/slb/port "13"
        client ena
        server ena
/c/slb/port "14"
        client ena
        server ena
/c/slb/port "15"
        client ena
        server ena
/c/slb/port "16"
        client ena
        server ena
/c/slb/port "17"
        client ena
        server ena
/c/slb/port "18"
        client ena
        server ena
/c/slb/port "19"
        client ena
        server ena
/c/slb/port "20"
        client ena
        server ena
/c/slb/port "21"
        client ena
        server ena
/c/slb/port "22"
        client ena
        server ena
/c/slb/port "23"
        client ena
        server ena
/c/slb/port "24"
        client ena
        server ena
/c/slb/port "25"
        client ena
        server ena
/c/slb/port "26"
        client ena
        server ena
"""

filter_data_input = """
/c/slb/filt 1
        ena
        action allow
        ipver v4
        sip any
        smask 0.0.0.0
        dip 224.0.0.0
        dmask 240.0.0.0
        group 1
        rport 0
        vlan any
/c/slb/filt 2
        ena
        action allow
        ipver v4
        sip any
        smask 0.0.0.0
        dip any
        dmask 0.0.0.0
        proto icmp
        group 1
        rport 0
        vlan any
/c/slb/filt 3
        ena
        action allow
        ipver v4
        sip any
        smask 0.0.0.0
        dip any
        dmask 0.0.0.0
        proto tcp
        sport dns
        group 1
        rport 0
        vlan any
/c/slb/filt 4
        ena
        action allow
        ipver v4
        sip any
        smask 0.0.0.0
        dip any
        dmask 0.0.0.0
        proto udp
        sport dns
        group 1
        rport 0
        vlan any
/c/slb/filt 2048
        ena
        action deny
        ipver v4
        sip any
        smask 0.0.0.0
        dip any
        dmask 0.0.0.0
        group 1
        rport 0
        vlan any
"""

# Transform and print the output with log_mode set to "disable"
transformed_output = transform_filter_data(filter_data_input, port_data_input, log_mode="disable")
print(transformed_output)


## firewall policy는 생성되지 않습니다. 직접 입력해주셔야 합니다.