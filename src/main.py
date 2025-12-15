# Arianna Abramovich
# ASTE404
# main.py

"""
What this file is responsible for:
How do I run the simulation and visualize the results?
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

from model import reentry_odes
from integrator import rk4_step


# Physical parameters
params = {
    'g': 9.80665,  # gravity [m/s^2]
    'Cd': 1.2,     # drag coefficient [-]
    'A': 10.0,     # reference area [m^2]
    'm': 2000.0    # vehicle mass [kg]
}

# Initial conditions
h0 = 120e3   # altitude from eath's surface [m]
V0 = 7500.0  # downward velocity [m/s]
T0 = 0.0     # thermal load - initially, no heat has been absorbed

y = np.array([h0, V0, T0])

# Time integration setup
dt = 0.5   # time step [s]
t = 0.0

# stores histories to plot later
history = {
'h': [],
'V': [],
'T': []
}

# Time-marching loop - stop at 1km 
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

print("Plotting now...")


# ----------------
#      PLOTS  
# ----------------        

# Velocity vs. Altitude [km]
plt.figure()
plt.plot(V, h / 1000) 
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.xlabel('Velocity [m/s]')
plt.ylabel('Altitude [km]')
plt.title('Velocity vs. Altitude')
plt.show()

# Deceleration due to Drag
plt.figure()
time = np.arange(len(V)) * dt

# Ground impact point (last time step)
t_ground = time[-1]
V_ground = V[-1]

# Ground impact marker
plt.scatter(t_ground, V_ground, color='red', zorder=5)
plt.axvline(t_ground, linestyle='--', alpha=0.6)

plt.annotate(
    'Ground Impact',
    xy=(t_ground, V_ground),
    xytext=(t_ground*0.65, 0.2*max(V)),
    arrowprops=dict(arrowstyle='->')
)
# Compute atmospheric density and drag acceleration
rho = np.array([np.exp(-hi / 8500.0) * 1.225 for hi in h])
a_drag = 0.5 * params['Cd'] * params['A'] / params['m'] * rho * V**2

# Find index where drag first exceeds gravity
idx_drag_dom = np.where(a_drag > params['g'])[0][0]

t_drag = time[idx_drag_dom]
V_drag = V[idx_drag_dom]

# Drag-dominant annotation
plt.scatter(t_drag, V_drag, color='purple', zorder=5)

plt.annotate(
    'Drag Deceleration Begins',
    xy=(t_drag, V_drag),
    xytext=(t_drag*1.5, V_drag*0.8),
    arrowprops=dict(arrowstyle='->')
)

plt.plot(time, V,color='gray', label='Velocity')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.title('Velocity vs Time During Re-entry')
plt.legend(loc='upper right')
plt.show()

# Thermal Load vs. Altitude [km]
plt.figure()
plt.plot(T, h / 1000)
plt.gca().invert_yaxis()
plt.xlabel('Accumulated Thermal Load [J/m^2]')
plt.ylabel('Altitude [km]')
plt.title('Thermal Load vs. Altitude')
plt.show()

# Thermal Load vs. Velocity and Altitude (shows trajection of rocket)
# Create grid
V_grid = np.linspace(min(V), max(V), 200)
h_grid = np.linspace(min(h), max(h), 200)
V_mesh, h_mesh = np.meshgrid(V_grid, h_grid)

# Interpolate T onto the grid
T_grid = griddata((V, h), T, (V_mesh, h_mesh), method='linear')

plt.figure()
plt.pcolormesh(V_mesh, h_mesh/1000, T_grid, shading='auto', cmap='inferno')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.xlabel('Velocity [m/s]')
plt.ylabel('Altitude [km]')
plt.title('Thermal Load vs. Velocity and Altitude')
plt.colorbar(label='Accumulated Thermal Load [J/m^2]')
plt.show()