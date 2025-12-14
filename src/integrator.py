# Arianna Abramovich
# ASTE404
# integrator.py

"""
What this file is responsible for:
Given an ODE system, how do I advance the solution forward in time?
"""

import numpy as np

def rk4_step(f, t, y, dt, params):
   # Parameters
        # f: function returning dy/dt = f(t, y, params)
        # t: current time [s]
        # y: current state vector
        # dt: time step [s]
        #params: dictionary of physical parameters

    k1 = f(t, y, params)                        # slope @ beginning interval
    k2 = f(t + dt/2, y + dt/2 * k1, params)     # slope @ midpoint
    k3 = f(t + dt/2, y + dt/2 * k2, params)     # improved midpoint slope
    k4 = f(t + dt, y + dt * k3, params)         # slope at the end of the interval

    y_next = y + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)   # weighted average 

    return y_next