import os
import fnmatch
from subprocess import call
import sys

tgt =  "/home/fpereira/working_now/MotoTestsDLOG/dlog_fernando/TestsModel/PUSCH/Tests_Done_20_04/Test/"

expected_pks = 1000
target_dir = tgt

#target_dir = "/home/fpereira/working_now/MotoTestsDLOG/dlog_fernando/TestsModel/PDSCH/T10_27_04/csv/"

#output = target_dir + "means.csv"

output = "/home/fpereira/working_now/motoresults/T1p_-30.csv"

format_in = ".csv"
op_path = "/home/fpereira/working_now/MotoCsvKey/csvMean/csvMeanPeakutils.py"

call( [ "python", "serial_DlogToBareCsv.py", tgt])

for subdir, dirs, files in os.walk(target_dir, followlinks=True):
    for f in files:
        if f.endswith(format_in):
            tgtf = target_dir + f
            call(["python", op_path, tgtf, output, str(expected_pks)])

