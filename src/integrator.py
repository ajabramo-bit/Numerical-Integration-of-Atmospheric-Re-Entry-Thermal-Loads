# Arianna Abramovich
# ASTE404
# integrator.py

import numpy as np

def rk4_step(f, t, y, dt, params):
    """
    Perform a single 4th-order Runge–Kutta step.


    Parameters
    ----------
    f : function
    Function returning dy/dt = f(t, y, params)
    t : float
    Current time [s]
    y : ndarray
    Current state vector
    dt : float
    Time step [s]
    params : dict
    Dictionary of physical parameters


    Returns
    -------
    ndarray
    Updated state vector after dt
    """

k1 = f(t, y, params)
k2 = f(t + dt/2, y + dt/2 * k1, params)
k3 = f(t + dt/2, y + dt/2 * k2, params)
k4 = f(t + dt, y + dt * k3, params)

return y + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)