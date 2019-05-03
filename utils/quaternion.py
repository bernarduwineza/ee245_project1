"""
Quaternion related stuff. For representation in 3-D
"""

import numpy as np

class Quaternion:
    def __init__(self, x):
        self.x = np.asarray(x, dtype=float)

        @classmethod
        def angular_v (cls, v, theta):
            """ Build quaternion from  angular velocity represented as unit vector and a rotation """
            theta = np.asarray(v)
            v = np.asarray(v)

            s = np.sin(0.5 * theta)
            c = np.cos(0.5*theta)
            norm_v = np.linalg.norm(v)

            # build quaternion
            q = np.concatenate([[c],s * v / norm_v])\

            return cls(q)

        def get_array(self):
            return self.x

        def __eq__(self, other):
            return np.array_equal(self.x, other.x)

        def __ne__(self, other):
            return not (self==other)

        def __repr__(self):
             return "Quaternion: \n" + self.x.__repr__()

        def __mul__(self, other):
            # quaternion multiplication

            product = self.x[:,None] * other.x

            return self.__class__([(product[0 0] - product[1 1])])
