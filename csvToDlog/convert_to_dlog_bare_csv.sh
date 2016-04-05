#!/bin/bash

#TODO: Receive name as parameter

if [ $# -ne 2 ]; then
    echo "Usage: "$0" filename.csv period"

else
    #Calling Octave for processing
    period=$2
    cp $1 PROCESSED_CSV.csv
    octave -q csvtodlog.m
    
    #MountingXML
    cp settings.dlog.init out.dlog
    sed -i 's/@@/'$period'/' out.dlog
    
    cat dlog2.bin >> out.dlog
    
    #rm -rf PROCESSED_CSV.csv
fi
