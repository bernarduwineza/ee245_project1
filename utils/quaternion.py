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

        prod = self.x[:, None] * other.x

        return self.__class__([(prod[0, 0] - prod[1, 1]
                                - prod[2, 2] - prod[3, 3]),
                               (prod[0, 1] + prod[1, 0]
                                + prod[2, 3] - prod[3, 2]),
                               (prod[0, 2] - prod[1, 3]
                                + prod[2, 0] + prod[3, 1]),
                               (prod[0, 3] + prod[1, 2]
                                - prod[2, 1] + prod[3, 0])])

    def as_v_theta(self):
        """Return the v, theta equivalent of the (normalized) quaternion"""
        # compute theta
        norm = np.sqrt((self.x ** 2).sum(0))
        assert (norm != 0)
        theta = 2 * np.arccos(self.x[0] / norm)

        # compute the unit vector
        v = np.array(self.x[1:], order='F', copy=True)
        length = np.sqrt(np.sum(v ** 2, 0))
        if length > 0.0:
            v /= length
        return v, theta

    def as_rotation_matrix(self):
        """Return the rotation matrix of the (normalized) quaternion
           https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
           Improving computation speed https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4435132/
           """
        v, theta = self.as_v_theta()
        c = np.cos(theta)
        s = np.sin(theta)

        return np.array([[v[0] * v[0] * (1. - c) + c,
                          v[0] * v[1] * (1. - c) - v[2] * s,
                          v[0] * v[2] * (1. - c) + v[1] * s],
                         [v[1] * v[0] * (1. - c) + v[2] * s,
                          v[1] * v[1] * (1. - c) + c,
                          v[1] * v[2] * (1. - c) - v[0] * s],
                         [v[2] * v[0] * (1. - c) - v[1] * s,
                          v[2] * v[1] * (1. - c) + v[0] * s,
                          v[2] * v[2] * (1. - c) + c]])
