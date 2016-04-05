#!/bin/bash

#TODO: Receive name as parameter

if [ $# -ne 1 ]; then
    echo "Usage: "$0" filename.csv"

else    
    #Calling Octave for processing
    octave -q ./csvStatistics/csvTrim.m $1
fi
