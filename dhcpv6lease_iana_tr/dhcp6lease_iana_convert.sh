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


  filename="backup-2025-08-13.tar.gz"

echo ${filename#-}


  filename="backup-2025-08-13.tar.gz"

echo ${filename#-*}