import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import peakutils

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





# search_space = 10E-3 #s
# period = 2.048E-5 #s
# desloc_lim = int(math.ceil(search_space/period))
# search_depth = desloc_lim #Ate onde olhar para minimizacao?

# start_s = desloc_lim  #Posicao para inicia pesquisa

# print "\tLim Desl: %d\n\tSearch Depth %d" % (desloc_lim,search_depth)
# print "\tSizeofB: %d" % len(B[0])
# sq_error = []
# for offset in range(-desloc_lim,desloc_lim):
#     v = 0
#     for i in range(search_depth)
#         a = A[1][(start_s+i)]
#         b = B[1][(start_s+offset+i)]
#         _ = math.pow(a-b,2)
#         if (a >= 0.16) or (b >= 0.16): 
#             v += _
#     sq_error.append( v )
# #    print "Error for offset %d : %f" % (offset, v)

# #err_min = min(sq_error)
# #print sq_error
# index_min = np.argmin(sq_error)
# desloc_time = (index_min-desloc_lim)*period

# print "Desl indice: %d  -- tempo %f" % (index_min, desloc_time)
# #print "Erro: %f " % (err_min)



# # a = [ x+desloc_time for x in B[0] ] 
# # B = [a,B[1]]

# offset = index_min - desloc_lim
# if offset < 0:
#     a = A[0][-offset:]
#     b = B[1][:offset]
#     B = [a,b]
#     print "MENOR!"
# else:
#     a = A[0][:offset]
#     b = B[1][-offset:]
#     B = [a,b]
#     print "Maior!"

# plt.plot(A[0],A[1], 'r', B[0],B[1], 'b')
# plt.show()

# plt.plot(B[0],B[1], 'r',C[0],C[1], 'b')
# plt.show()

# #--------------------------





