#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This script converts a default KeySight dlog file to a KeySight csv"
    echo "Output: out.csv and out_bare.csv"
    echo "Usage: "$0" filename.csv"
else
    temp_file="temp.bin"
    cp $1 $temp_file
    period=`grep -aoe "<tint>.*</tint>" $temp_file` 
    period=`echo $period | cut -d ">" -f2 | cut -d "<" -f1`

    time=`grep -aoe "<time>.*</time>" $temp_file` 
    time=`echo $time | cut -d ">" -f2 | cut -d "<" -f1`

    echo "Time: "$time" Period: "$period" Values: `expr $time / $period`"

    killpoint=1
    while read line    
    do
	isEnd=`echo $line | grep -c "</dlog>"`
	if [ $isEnd -gt 0 ] 
	then
	    break
	fi
	killpoint=`expr $killpoint + 1`
    done < $temp_file

    cm="1,$killpoint""d"
    echo $cm
    sed -i $cm $temp_file

    octave -q ./dlogToCsv/dlogToCsv.m $temp_file $period out_bare.csv
    cp ./dlogToCsv/csv_header.init ./out.csv
    sed -i 's/@@/'$period'/' out.csv

    cat ./out_bare.csv >> out.csv
    rm -rf temp.bin
fi
