import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import peakutils

period = 2.048E-5 #s
md = 3.0E-3/period
slc_beg = 0
slc_end = 5000
a,b = np.loadtxt('Exemplo.csv', delimiter=',', usecols=(0,1), unpack=True, dtype=float)
A=[a[slc_beg:slc_end],b[slc_beg:slc_end]]

a,b = np.loadtxt('Exemplo2.csv', delimiter=',', usecols=(0,1), unpack=True, dtype=float)
B=[a[slc_beg:slc_end],b[slc_beg:slc_end]]

#plt.plot(A[0], A[1], "g", B[0], B[1], "b")
#plt.show()

#define slices for checking parameters
chk_beg = 1
chk_end = 3000


ma = max(A[1][chk_beg:chk_end])
ind_peak_a = peakutils.indexes(A[1][chk_beg:chk_end], thres=0.9, min_dist=md)
pk_v_a = [ A[1][x] for x in ind_peak_a]
pk_t_a = [ A[0][x] for x in ind_peak_a]
#plt.plot(A[0], A[1], "g", pk_t_a, pk_v_a, "*r")
#plt.show()


#TEST_FEATURE
expected_pks = int(math.floor((chk_end-chk_beg)*period/(10.0E-3)))
ind_peak_b = peakutils.indexes(B[1][chk_beg:chk_end], thres=0.5)
pk_v_b = [ B[1][x] for x in ind_peak_b]
pk_t_b = [ B[0][x] for x in ind_peak_b]
pk_v_b.sort()
pk_draft = pk_v_b

for i in range(len(pk_v_b)):
    pk_v_b[i] = pk_draft[len(pk_v_b)-1-i]

centroid = []
radius = []
for i in range((len(pk_v_b)-expected_pks)):
    min_interv = min(pk_v_b[i:i+expected_pks])
    max_interv = max(pk_v_b[i:i+expected_pks])
    centroid.append( 0.5*(max_interv+min_interv))
    radius.append  ( 0.5*(max_interv-min_interv))

print(radius)
plt.plot(B[0], B[1], "g")
plt.show()

plt.plot(radius)
plt.show()

inv_radius = [1./x for x in radius]
num_pks = len(inv_radius)
imax = inv_radius.index(max(inv_radius[1:int(0.05*num_pks)]))


for i in range(imax-1):
    indexOutOfBound = np.where( B[1]==pk_v_b[i])
    B[1][indexOutOfBound] = 0.14

plt.plot(inv_radius)
plt.show()

#/TEST_FEATURE
ind_peak_b = peakutils.indexes(B[1][chk_beg:chk_end], thres=0.9, min_dist=md)
pk_v_b = [ B[1][x] for x in ind_peak_b]
pk_t_b = [ B[0][x] for x in ind_peak_b]
plt.plot(B[0], B[1], "g", pk_t_b, pk_v_b, "*r")
plt.show()

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

plt.plot(REF[0], REF[1], "g", LAT[0], LAT[1], "b")
plt.show()


 
