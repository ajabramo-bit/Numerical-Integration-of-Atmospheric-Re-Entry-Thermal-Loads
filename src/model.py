# Arianna Abramovich
# ASTE404
# model.py

"""
What this file is responsible for:
What equations govern atmospheric re-entry?
"""

import numpy as np

def atmospheric_density(h, rho0=1.225, H=8500.0):
    # Exponential atmosphere model

    rho_h = rho0 * np.exp(-h/H)
        # h: altitude (float) [m]
        # rho0: sea-level density (float) [kg/m^3]
        # H: scale height (float) [m]

    return rho_h


def sutton_graves_heating(rho, V, k=1.83e-4):
    # Sutton–Graves stagnation-point heating correlation

    q_dot = k * np.sqrt(rho) * abs(V)**3
        # k: Sutton-Graves coefficient 
        # rho: atmospheric density (float) [kg/m^3]
        # V: velocity [m/s]                                                                            
    return q_dot


def reentry_odes(t, y, params):
    # Coupled ODE system for 1D atmospheric re-entry.
        # State vector:
        # y[0] = h : altitude [m]
        # y[1] = V : downward velocity [m/s]
        # y[2] = T : accumulated thermal load [arbitrary units]
    
    h, V, T = y
    rho_h = atmospheric_density(h)

    # Kinematics
    dhdt = -V

    # Dynamics (gravity + drag)
    drag = 0.5 * params['Cd'] * params['A'] / params['m'] * rho_h * V**2
    dVdt = params['g'] - drag

    # Thermal response (integrated heating)
    q_dot = sutton_graves_heating(rho_h, V)
    dTdt = q_dot

    return np.array([dhdt, dVdt, dTdt])