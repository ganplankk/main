from scapy.layers.dhcp6 import *

# 서버 IP와 포트 지정
target_ip = "2001:db8:1::200"
target_port = 547

# DHCPv6 SOLICIT 패킷 생성
pkt = (
    IPv6(dst=target_ip) /
    UDP(sport=546, dport=target_port) /
    DHCP6_Solicit(trid=0x123456) /
    DHCP6OptClientId(duid=DUID_LL(lladdr="00:11:22:33:44:55")) /
    DHCP6OptIA_NA(iaid=1, T1=600, T2=900)
)

send(pkt)
