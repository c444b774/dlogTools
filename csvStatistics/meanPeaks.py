import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal.find_peaks_cwt

with open("P1.csv", 'r') as dest_f:
    data_it =  csv.reader(dest_f, delimiter = ',')
    data = [data for data in data_it]
data_array = np.asarray(data)

data_array = data_array[1:10000,:]


#plt.plot(data_array[:,1])
#plt.show()




