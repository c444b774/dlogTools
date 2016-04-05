import csv
import numpy as np
import matplotlib.pyplot as plt
import math

#end = 110

a,b = np.loadtxt('Comparison1.csv', delimiter=',', usecols=(0,1), unpack=True, dtype=float)
A=[a[:],b[:]]

a,b = np.loadtxt('Comparison2.csv', delimiter=',', usecols=(0,1), unpack=True, dtype=float)
B=[a[:],b[:]]

C = B[:]

plt.plot(A[1])
plt.plot(B[1])
plt.show()


# # Bloco 1: Acha o valor do deslocamento que minimiza 
# #          a distancia em tempo entre os arquivos
# stt_p = A[0][0] #T0 do arquivo A (primeiro Ponto)
# min_v = 1000000 #Valor 
# min_i = 0
# for time_offset in range(len(B[0])):
#     if min_v >= abs(stt_p - B[0][time_offset]):
#         min_v = abs(stt_p - B[0][time_offset])
#         min_i = time_offset

# print "Time offset for B: %f" % time_offset

# for i in range(len(B[0])-time_offset):
#     B[0][i] = B[0][i+time_offset]
#     B[1][i] = B[1][i+time_offset]

# print B


search_space = 10E-3 #s
period = 2.048E-5 #s
desloc_lim = int(math.ceil(search_space/period))
search_depth = desloc_lim #Ate onde olhar para minimizacao?

start_s = desloc_lim  #Posicao para inicia pesquisa

print "\tLim Desl: %d\n\tSearch Depth %d" % (desloc_lim,search_depth)
print "\tSizeofB: %d" % len(B[0])
sq_error = []
for offset in range(-desloc_lim,desloc_lim):
    v = 0
    for i in range(search_depth):
        a = A[1][(start_s+i)]
        b = B[1][(start_s+offset+i)]
        _ = math.pow(a-b,2)
        if (a >= 0.16) or (b >= 0.16): 
            v += _
    sq_error.append( v )
#    print "Error for offset %d : %f" % (offset, v)

#err_min = min(sq_error)
#print sq_error
index_min = np.argmin(sq_error)
desloc_time = (index_min-desloc_lim)*period

print "Desl indice: %d  -- tempo %f" % (index_min, desloc_time)
#print "Erro: %f " % (err_min)



# a = [ x+desloc_time for x in B[0] ] 
# B = [a,B[1]]

offset = index_min - desloc_lim
if offset < 0:
    a = A[0][-offset:]
    b = B[1][:offset]
    B = [a,b]
    print "MENOR!"
else:
    a = A[0][:offset]
    b = B[1][-offset:]
    B = [a,b]
    print "Maior!"

plt.plot(A[0],A[1], 'r', B[0],B[1], 'b')
plt.show()

plt.plot(B[0],B[1], 'r',C[0],C[1], 'b')
plt.show()

#--------------------------





