#!/bin/sh
WORK_DIR=/path/to/workdir
spawn-fcgi -d $WORK_DIR -f $WORK_DIR/mail-sender-web-service.py -a 127.0.0.1 -p 1110

