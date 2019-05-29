from utils import mapping
import numpy as np

data = np.array([20, 20, 40, 10, 10, 10])
data = data.reshape((1, 6))
print(np.shape(data))

filename = 'sample_obs.csv'
data = np.loadtxt(filename, delimiter=',', dtype='Float64', skiprows=2)

voxmap = mapping.create_voxmap(data, 2)

mapping.visualise_voxmap(voxmap)

