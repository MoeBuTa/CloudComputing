#!/bin/bash
function timediff() {
    start_time=$1
    end_time=$2
    start_s=${start_time%.*}
    start_nanos=${start_time#*.}
    end_s=${end_time%.*}
    end_nanos=${end_time#*.}
    if [ "$end_nanos" -lt "$start_nanos" ];then
        end_s=$(( 10#$end_s - 1 ))
        end_nanos=$(( 10#$end_nanos + 10**9 ))
    fi
    time=$(( 10#$end_s - 10#$start_s )).$(( (10#$end_nanos - 10#$start_nanos)/10**6 ))
    echo $time
}
start=$(date +"%s.%N")
python3 fileencrypt.py
end=$(date +"%s.%N")
echo "Total execution time for custom solution:"
timediff $start $end
start=$(date +"%s.%N")
python3 fileencrypt.py
end=$(date +"%s.%N")
echo "Total execution time for using KSM:"
timediff $start $end

