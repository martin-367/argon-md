# core simulation logic
import numpy as np
import math

N = 100 # number of particles
L = 10.0 # box size
dt = 0.01 # time step
steps = 1000 # number of steps
dim = 3 # spatial dimensions

# particle characteristics
r = 0.1
m = 1



def initialize_positions(N, L):
  # [x1, y1, z1; x2, y2, v2...]
  return np.random.rand(N, 3) * L # randn(i, j) creates a matrix of i rows and j columns with random numbers between 0 and 1

def initialize_velocities(N):
  v = np.random.randn(N, 3) # randN is a random distribution (mean 0, std = 1)
  v -= np.mean(v, axis = 0) # remove net momentum (calculate average velocity of all partices and subtract from every individual particles velocity)
  # removing net momentum removes initial artificial drift of molecules
  
  return v

def compute_forces(positions, L):
  forces = np.zeros_like(positions) #initialize forces to zero with same shape as positions matrix
  for i in range(N):
    for j in range(i + 1, N): #only compute each pair once
      pass
      #simple bounce collision
      distance = math.dist(positions[i], positions[j])
      if distance < 2 * r:
        direction = (positions[i] - positions[j]) / distance
        forces[i] += direction
        forces[j] -= direction
  return forces


def velocity_verlet(positions, velocities, forces, dt, L):
  #update positions and velocities
  positions += velocities * dt + 0.5 * forces * dt**2
  positions %= L # apply periodic boundary conditions

  new_forces = compute_forces(positions, L)
  velocities += 0.5 * (forces + new_forces) * dt / m
  
  return positions, velocities, forces
