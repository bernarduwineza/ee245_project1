from utils import mapping
import numpy as np
import io
import sys

filepath = sys.argv[1]

filepath = 'SampleEnvironment.txt'
s = open('SampleEnvironment.txt').read().replace(':', ';')

data = np.loadtxt(io.StringIO(s), delimiter=';', dtype='Float64', comments='#', skiprows=2)


grid = mapping.create_grid(data, 0.1)


# mapping.visualise_voxmap(voxmap)

