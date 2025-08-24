from src import md
import matplotlib.pyplot as plt

positions = md.initialize_positions(N, L)
velocities = md.initialize_velocities(N)
forces = md.compute_forces(positions, L)

energy_log = []
temp_log = []

for step in range(md.steps):
  positions, velocities, forces = md.velocity_verlet(positions, velocities, forces, dt, L)
  energy_log.append(md.compute_kinetic_energy(velocities))
  temp_log.append(md.compute_temperature(velocities))

# Plotting

plt.plot(energy_log)
plt.plot(temp_log)
plt.show()

# periodic boundary conditions
# implement neighbour lists
# introduce thermostats (berendsen or langevin
# export trajectories for visualization in VMD or OVITO
