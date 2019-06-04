from utils import mapping
import numpy as np
import io
import sys
import time

start_t = time.perf_counter()
filepath = 'SampleEnvironment.txt'
s = open(filepath).read().replace(':', ';')

""" Assuming the obstacles begin after two lines as indicated in the sample file 
    It is also assumed that no line is blank after the second intentional blank line
"""
size = s.splitlines()[0]

size = np.loadtxt(io.StringIO(size), delimiter=';', dtype='Float64', comments='#')

data = np.loadtxt(io.StringIO(s), delimiter=';', dtype='Float64', comments='#', skiprows=2)
grid_res = 0.1

grid = mapping.create_grid(data, grid_res, size)
end_t = time.perf_counter()
elapsed_time = end_t - start_t
print('Done... in', elapsed_time, 'seconds')

