import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import peakutils

period = 2.048E-5 #s
slc_beg = 0
slc_end = 5000
a,b = np.loadtxt('Comparison1.csv', delimiter=',', usecols=(0,1), unpack=True, dtype=float)
A=[a[slc_beg:slc_end],b[slc_beg:slc_end]]

a,b = np.loadtxt('Comparison2.csv', delimiter=',', usecols=(0,1), unpack=True, dtype=float)
B=[a[slc_beg:slc_end],b[slc_beg:slc_end]]

plt.plot(A[1])
plt.plot(B[1])
#plt.show()


#define slices for checking parameters
chk_beg = 1
chk_end = 3000

ind_peak_a = peakutils.indexes(A[1][chk_beg:chk_end])
ind_peak_b = peakutils.indexes(B[1][chk_beg:chk_end])

mean_dist_a = 0
mean_dist_b = 0


for i in range(2,len(ind_peak_a)+1):
    mean_dist_a += ind_peak_a[-i+1] - ind_peak_a[-i]
mean_dist_a /= float(len(ind_peak_a))

for i in range(2,len(ind_peak_b)+1):
    mean_dist_b += ind_peak_b[-i+1] - ind_peak_b[-i]
mean_dist_b /= float(len(ind_peak_b))

#debug
print "Mean dist:\n\ta: %f\n\tb: %f" % (mean_dist_a, mean_dist_b)
print ind_peak_a
print ind_peak_b

if not ((mean_dist_a > 0.9*mean_dist_b) and (mean_dist_a < 1.1*mean_dist_b)):
    print "Not suitable"
    exit

REF  = 0       # Reference setpoint
REF_pk = 0
LAT = 0        # Late setpoint
LAT_pk = 0
if mean_dist_a<= mean_dist_b:
    REF = A
    REF_pts = ind_peak_a
    LAT = B
    LAT_pk = ind_peak_b
else:
    REF = B
    REF_pk = ind_peak_b
    LAT = A
    LAT_pk = ind_peak_a

dst_t = (LAT_pk[0] - REF_pk[0])*period

LAT[0] = [ x - dst_t for x in LAT[0] ]


