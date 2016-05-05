import os
import fnmatch
from subprocess import call
import sys

target_dir = sys.argv[1] #"/home/fpereira/working_now/MotoTestsDLOG/dlog_fernando/TestsModel/PUSCH/TestsDone_15_04/Test7_15_04/Band4/"

output_dir = target_dir #"/home/fpereira/working_now/MotoTestsDLOG/dlog_fernando/TestsModel/PUSCH/TestsDone_15_04/Test7_15_04/Band4/csv/"
#target_dir = "/home/fpereira/working_now/MotoTestsDLOG/dlog_fernando/TestsModel/PDSCH/T10_27_04/"
#output_dir = "/home/fpereira/working_now/MotoTestsDLOG/dlog_fernando/TestsModel/PDSCH/T10_27_04/csv/"

format_in = ".dlog"
format_out = ".csv"

op_path = "/home/fpereira/working_now/MotoCsvKey/dlogToBareCsvCustom.sh"


for subdir, dirs, files in os.walk(target_dir, followlinks=True):
    for f in files:
        if f.endswith(format_in):
            tgtf = target_dir + f
            call([op_path, tgtf, (os.path.splitext(tgtf)[0]+format_out) ])


#call( [ "mv", target_dir+"*.csv", output_dir])

# standard_in) 1: syntax error
# Time: 10 Period: 2.048e-05 Values: 
# 1,52d
# error: no such file, '/home/fpereira/Dropbox/working_NOW/MotoCsvKey/csvMean/dlogToCsv/dlogToCsv.m'
# error: source: error sourcing file '/home/fpereira/Dropbox/working_NOW/MotoCsvKey/csvMean/dlogToCsv/dlogToCsv.m'
# cat: ./out_bare.csv: No such file or directory
# (standard_in) 1: syntax error

