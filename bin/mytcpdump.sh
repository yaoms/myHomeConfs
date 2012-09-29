#!/bin/bash

tcpdump -i eth0 -n -vv -X -s0 'tcp port 80 and host 124.172.168.97' | tee tcpdump.txt

# clgr0kw4

# 25410834
