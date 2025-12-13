# Arianna Abramovich
# ASTE404
# main.py

import numpy as np
import matplotlib.pyplot as plt
from model import reentry_odes
from integrator import rk4_step


# Physical parameters
params = {
'g': 9.81, # gravity [m/s^2]
'Cd': 1.2, # drag coefficient [-]
'A': 10.0, # reference area [m^2]
'm': 2000.0 # vehicle mass [kg]
}

# Initial conditions
h0 = 120e3 # altitude [m]
V0 = 7500.0 # downward velocity [m/s]
T0 = 0.0 # thermal load

y = np.array([h0, V0, T0])

# Time integration setup
dt = 0.5 # time step [s]
t = 0.0

history = {
'h': [],
'V': [],
'T': []
}

# Time-marching loop
while y[0] > 1000.0:
    history['h'].append(y[0])
    history['V'].append(y[1])
    history['T'].append(y[2])

y = rk4_step(reentry_odes, t, y, dt, params)
t += dt

# Convert lists to arrays
h = np.array(history['h'])
V = np.array(history['V'])
T = np.array(history['T'])

# Plot results
plt.figure()
plt.plot(V, h / 1000)
plt.gca().invert_yaxis()
plt.xlabel('Velocity [m/s]')
plt.ylabel('Altitude [km]')
plt.title('Velocity vs Altitude')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(T, h / 1000)
plt.gca().invert_yaxis()
plt.xlabel('Accumulated Thermal Load')
plt.ylabel('Altitude [km]')
plt.title('Thermal Load vs Altitude')
plt.grid(True)
plt.show()