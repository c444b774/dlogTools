#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This script prints mean period of sampling from a bareCsv file"
    echo "Usage: "$0" filename.csv"

else
    #Call octave script
    octave -q ./csvStatistics/bareCsvMeanPeriod.m $1
fi
