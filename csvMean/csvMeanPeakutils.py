import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import peakutils
import sys

debug = False

period = 2.048E-5 #s
measure_time = 1.0E-3 #s 
md = 0.9E-3/period
slc_beg = 0
slc_end = 30000

inf_pt_thr = 0.7
sup_pt_thr = 1.3
events_per_sec = 1.0

filename = sys.argv[1]
output = sys.argv[2]
a,b = np.loadtxt(filename, delimiter=',', usecols=(0,1), unpack=True, dtype=float)

if debug:
    A = [a[slc_beg:slc_end], b[slc_beg:slc_end]]
else:
    A = [a,b]

if debug:
    plt.plot(A[0], A[1], "g")
    plt.show()


expected_pks = int(sys.argv[3]) #max(A[0])/(events_per_sec*10.0E-3)

#define maximum
ind_peak_a = peakutils.indexes(A[1], thres=0.6, min_dist=md)

l_ipa = len(ind_peak_a)

### CUT SECTION
if l_ipa > 1300 or l_ipa < 700:
    print "This entry seems to have an error: " + str(l_ipa) + " points"
    plt.plot(A[0], A[1], "g")
    plt.show()
    beg = int(raw_input("startpoint (0:10): "))
    end = int(raw_input(" end point (0:10): "))

    beg *= len(A[0])/10
    end *= len(A[0])/10

    A[0] = A[0][beg:end]
    A[1] = A[1][beg:end]

    ind_peak_a = peakutils.indexes(A[1], thres=0.6, min_dist=md)

### ENDOFCUTTING

pk_v_a = [ A[1][x] for x in ind_peak_a]
pk_t_a = [ A[0][x] for x in ind_peak_a]

if debug:
    plt.plot(A[0], A[1], "g", pk_t_a, pk_v_a, "*r")
    plt.show()

#define parameters for measure
hcs = int(math.floor(0.5*(measure_time/period)))+1 #half chunk size

mean_pk_a = []
for peak in ind_peak_a:
    try:
        if peak > hcs and peak+hcs < len(A[1]):
            mean_pk_a.append(np.mean( A[1][(peak-hcs):(peak+hcs)] ))
    except IndexError:
        pass
mmean = np.mean(mean_pk_a)
mdp = np.std(mean_pk_a)

o=open(output,'a')
varnum = filename.split('__')[1]
print "\n " + filename
print "Peak Count: " + str(len(ind_peak_a)) + "\nMean: " + str(mmean) + "\nStd: " + str(mdp)
print >>o, filename+","+str(varnum)+","+str(len(ind_peak_a))+","+str(mmean)+","+str(mdp)
o.close()
