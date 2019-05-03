"""
author: Peter Huang
email: hbd730@gmail.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np

mass = 0.030     # kg
g = 9.81    # m/s/s
Ib = np.array([(1.43e-5, 0, 0),
              (0, 1.43e-5, 0),
              (0, 0, 2.89e-5)]);

invI = np.linalg.inv(Ib)
L = 0.046  # distance from  rotor axis to center of mass (m)
height = 0.05
minF = 0.0
maxF = 2.0 * mass * g
H = height
km = 1.5e-9     # thrust constant
kf = 6.11e-8    # moment constant
r = km / kf

#  [ F  ]         [ F1 ]
#  | M1 |  = A *  | F2 |
#  | M2 |         | F3 |
#  [ M3 ]         [ F4 ]
A = np.array([[1,  1,  1,  1],
              [0,  L,  0, -L],
              [-L,  0,  L,  0],
              [r, -r,  r, -r]])

invA = np.linalg.inv(A)

body_frame = np.array([(L, 0, 0, 1),
                       (0, L, 0, 1),
                       (-L, 0, 0, 1),
                       (0, -L, 0, 1),
                       (0, 0, 0, 1),
                       (0, 0, H, 1)])
