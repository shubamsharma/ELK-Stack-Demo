#!/bin/bash

cd /home/shubam/Downloads/elasticsearch-7.12.1/bin/
./elasticsearch &
sleep 120

cd /home/shubam/Downloads/kibana-7.12.1-linux-x86_64/bin/
./kibana &
sleep 120

cd /home/shubam/Downloads/logstash-7.12.1/bin
./logstash -r -f $3 &
sleep 180

#$2 give exact full path of log file
python3 $1/main_logstash.py $2


