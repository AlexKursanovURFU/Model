import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

with open('examples/out.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')
    data_read = [row for row in csv_read]

print(np.array(data_read))

names = data_read[0]
data = np.array(data_read[1:], dtype=np.float32)
print(names)
print(data)

x = data[:, 1]
y = data[:, 2]

peaks, _ = find_peaks(y, height=0)

time_duration = x[peaks[-1]] - x[peaks[-2]]
print(time_duration)

plt.plot(x,y)
plt.plot(x[peaks], y[peaks], "x")
plt.savefig('plot.png')