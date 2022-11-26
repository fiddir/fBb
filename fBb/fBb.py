#!/usr/bin/env python3

"""
An open source package to interpolate time series by multipoint fractional Brownian bridges 
url="https://github.com/fiddir/fBb"
license="MIT license"
"""

import numpy as np
from stochastic.processes.continuous import FractionalBrownianMotion

class MFBB:
    def __init__(self, X_i, t_i, H, N_fine, sigma=None): 
        self.X_i = X_i
        self.t_i = t_i
        self.H = H
        self.N_fine = N_fine
        self.N_coarse = np.size(X_i)
        if self.N_fine%self.N_coarse != 0:
            raise ValueError("Fine resolution N_fine must be multiples of number of prescribed points N_coarse")
        if sigma is None:
            self.sigma = np.sqrt(2*np.mean(self.X_i**2))/t_i[-1]**(H)
        else:
            self.sigma = sigma
        fbm = FractionalBrownianMotion(hurst=self.H, t=self.t_i[-1])
        self.X = fbm.sample(self.N_fine)
        self.t = fbm.times(self.N_fine)
        
    def cov(self, t, t_prime):
        T, T_prime = np.meshgrid(t, t_prime)
        return self.sigma**2*(T**(2*self.H)+T_prime**(2*self.H)-np.abs(T-T_prime)**(2*self.H))/2.
    
    def bridge(self):
        if 0. in self.t_i:
            raise ValueError("Please avoid zeros in t_i-array as it leads to singular inverse matrix in bridge construction.")
        coarse_points  = np.arange(1,self.N_coarse+1)*self.N_fine//self.N_coarse
        X_bridge = self.X - (self.X[coarse_points]-self.X_i)@np.linalg.inv(self.cov(self.t_i,self.t_i))@self.cov(self.t, self.t_i)
        return X_bridge
    
    def free(self):
        return self.X
        
    def t_fine(self):
        return self.t
    
    def t_coarse(self):
        return self.t_i







