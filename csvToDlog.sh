#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This script converts a default KeySight csv file to a KeySight dlog"
    echo "Output: out.dlog"
    echo "Usage: "$0" filename.csv"

else
    #Pre-processing: Take Period and remove headers
    period=`(sed -n '2,2 p' $1 | cut -d ':' -f2) | tr -d '\n' | tr -d '\r'`  #Gets the time between samplings

    cp $1 PROCESSED_CSV.csv
    sed -i '1,4d' ./csvToDlog/PROCESSED_CSV.csv
    
    #Calling Octave for processing
    octave -q ./csvToDlog/csvtodlog.m $1
    
    #MountingXML
    cp ./csvToDlog/settings.dlog.init out.dlog
    sed -i 's/@@/'$period'/' out.dlog
    
    cat ./csvToDlog/dlog2.bin >> out.dlog
    
    rm -rf PROCESSED_CSV.csv dlog2.bin
fi
