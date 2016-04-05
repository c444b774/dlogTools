import csv
import numpy as np
import matplotlib.pyplot as plt
import math

# with open("trimmed.csv", 'r') as dest_f:
#     data_it =  .reader(dest_f, delimiter = ',')
#     data = [float(data) for data in data_it]
#     type data_it
# A = np.asarray(data)

a,b = np.loadtxt('trimmed.csv', delimiter=',', usecols=(0,1), unpack=True, dtype=float)
B=[a,b]

period = 2.048E-5 #s
desloc_time = 5000*period

B[0] = [ x+desloc_time for x in B[0] ] 

with open('t.csv', 'w') as tf:
    csv_writer = csv.writer(tf)
    l = [ csv_writer.writerow([B[0][i],B[1][i] ]) for i in range(len(B[0])) ]
