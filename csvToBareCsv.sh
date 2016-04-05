#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This script converts a default KeySight csv file to a csv without readers readable by octave/matlab and prints the period of the sampling"
    echo "Output: out_bare.csv"
    echo "Usage: "$0" filename.csv"

else
    #Pre-processing: Take Period and remove headers
    period=`(sed -n '2,2 p' $1 | cut -d ':' -f2) | tr -d '\n' | tr -d '\r'`  #Gets the time between samplings

    cp $1 out_bare.csv
    sed -i '1,4d' out_bare.csv    
fi
