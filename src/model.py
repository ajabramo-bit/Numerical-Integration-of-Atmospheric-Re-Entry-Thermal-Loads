# Arianna Abramovich
# ASTE404
# model.py

import numpy as np

def atmospheric_density(h, rho0=1.225, H=8500.0):
    """
    Exponential atmosphere model.


    Parameters
    ----------
    h : float
    Altitude [m]
    rho0 : float
    Sea-level density [kg/m^3]
    H : float
    Scale height [m]


    Returns
    -------
    float
    Atmospheric density [kg/m^3]
    """

return rho0 * np.exp(-h / H)


def sutton_graves_heating(rho, V, k=1.83e-4):
    """
    Sutton–Graves stagnation-point heating correlation.


    q_dot = k * sqrt(rho) * V^3


    Parameters
    ----------
    rho : float
    Atmospheric density [kg/m^3]
    V : float
    Velocity magnitude [m/s]
    k : float
    Sutton–Graves coefficient (SI units)


    Returns
    -------
    float
    Heating rate (arbitrary thermal load units)
    """                                                                         
return k * np.sqrt(rho) * abs(V)**3


def reentry_odes(t, y, params):
    """
    Coupled ODE system for 1D atmospheric re-entry.


    State vector:
    y[0] = h : altitude [m]
    y[1] = V : downward velocity [m/s]
    y[2] = T : accumulated thermal load [arbitrary units]
    """
h, V, T = y


rho = atmospheric_density(h)


# Kinematics (velocity defined positive downward)
dhdt = -V

# Dynamics (gravity + drag)
drag = 0.5 * params['Cd'] * params['A'] / params['m'] * rho * V**2
dVdt = params['g'] - drag


# Thermal response (integrated heating)
q_dot = sutton_graves_heating(rho, V)
dTdt = q_dot


return np.array([dhdt, dVdt, dTdt])