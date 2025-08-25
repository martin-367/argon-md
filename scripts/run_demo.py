from src import md

import matplotlib.pyplot as plt

positions = md.initialize_positions(md.N, md.L)
velocities = md.initialize_velocities(md.N)
forces = md.compute_forces(positions, md.L)

energy_log = []
temp_log = []

for step in range(md.steps):
  positions, velocities, forces = md.velocity_verlet(positions, velocities, forces, md.dt, md.L)
  energy_log.append(md.compute_kinetic_energy(velocities))
  temp_log.append(md.compute_temperature(velocities))

# Plotting

plt.plot(energy_log)
plt.plot(temp_log)
plt.show()

# periodic boundary conditions
# implement neighbour lists
# introduce thermostats (berendsen or langevin)
# export trajectories for visualization in VMD or OVITO
