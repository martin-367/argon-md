from src import md

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from itertools import product, combinations

positions = md.initialize_positions(md.N, md.L)
velocities = md.initialize_velocities(md.N)
forces = md.compute_forces(positions, md.L)


def physics_step():
  global positions, velocities, forces
  positions, velocities, forces = md.velocity_verlet(positions, velocities, forces, md.dt, md.L)


# ------plotting------
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])
ax.set_xlim(0, md.L); ax.set_ylim(0, md.L); ax.set_zlim(0, md.L)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title('Molecular Dynamics Simulation')
#ax.set_proj_type('ortho')

def draw_box(ax, L):
  xs = [0, md.L]; ys = [0, md.L]; zs = [0, md.L]
  for s, e in combinations(np.array(list(product(xs, ys, zs))), 2):
      if np.sum(np.abs(s-e)) == xs[1]-xs[0] or np.sum(np.abs(s-e)) == ys[1]-ys[0] or np.sum(np.abs(s-e)) == zs[1]-zs[0]:
          ax.plot3D(*zip(s, e), color="k")

draw_box(ax, md.L)

size_scale = 100000
sizes = size_scale * md.r**3
scat = ax.scatter(positions[:,0], positions[:,1], positions[:,2], s=sizes, c='blue', alpha=0.6)

def animate(frame):
  physics_step()
  global positions, velocities, forces
  scat._offsets3d = (positions[:,0], positions[:,1], positions[:,2])
  return scat,


ani = FuncAnimation(fig, animate, frames=md.steps, interval=1000, blit=False)
plt.show()


# periodic boundary conditions
# implement neighbour lists
# introduce thermostats (berendsen or langevin)
# export trajectories for visualization in VMD or OVITO
