#!/bin/bash

if [ $# -ne 2 ]; then
    echo "This script converts a bare csv file to a KeySight dlog"
    echo "Output: out.dlog"
    echo "Usage: "$0" filename.csv period"

else
    #Calling Octave for processing
    octave -q ./csvToDlog/csvtodlog.m $1
    
    #MountingXML
    cp ./csvToDlog/settings.dlog.init out.dlog
    sed -i 's/@@/'$2'/' out.dlog
    
    cat ./csvToDlog/dlog2.bin >> out.dlog
fi
