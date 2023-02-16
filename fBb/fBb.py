#!/usr/bin/env python3

"""
An open source package to interpolate time series by multipoint fractional Brownian bridges 
url="https://github.com/fiddir/fBb"
license="MIT license"
"""

import numpy as np
from stochastic.processes.continuous import FractionalBrownianMotion

class MFBB:
    def __init__(self, X_i, t_i, H, dt, sigma=None): 
        self.X_i = X_i
        self.t_i = t_i
        self.H = H
        self.dt = dt
        self.N_fine = np.int(self.t_i[-1]/self.dt)
        self.N_coarse = np.size(X_i)
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
        if all(np.array([round(entry,10).is_integer() for entry in (self.t_i/self.dt)])) == False:
            raise ValueError("Choice of time step dt does not match values in t_i-array")
        if 0. in self.t_i:
            raise ValueError("Please avoid zeros in t_i-array as it leads to singular inverse matrix in bridge construction.")
        #coarse_points  = np.arange(1,self.N_coarse+1)*self.N_fine//self.N_coarse
        index = np.isin(np.array([round(t_entry,10) for t_entry in self.t]), self.t_i)
        coarse_points = np.where(index)
        X_bridge = self.X - (self.X[coarse_points]-self.X_i)@np.linalg.inv(self.cov(self.t_i,self.t_i))@self.cov(self.t, self.t_i)
        return X_bridge
    
    def free(self):
        return self.X
        
    def t_fine(self):
        return self.t
    
    def t_coarse(self):
        return self.t_i







