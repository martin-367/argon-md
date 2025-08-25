# core simulation logic
import numpy as np

N = 100 # number of particles
L = 10.0 # box size
dt = 0.01 # time step
steps = 1000 # number of steps
dim = 3 # spatial dimensions

# lennard-jones parameters
epsilon = 1.0 # depth of the potential well
sigma = 1.0 # finite distance at which the inter-particle potential is zero
cutoff = 2.5 * sigma # cutoff distance for the potential


def initialize_positions(N, L):
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
      #compute distance vector between particles i and j with periodic boundary conditions
      rij = positions[i] - positions[j] # distance vector
      rij -= L * np.round(rij / L) # periodic boundary conditions
      r = np.linalg.norm(rij) # magnitude of distance vector

      if r < cutoff:
        f_mag = 24*epsilon * (2 * (sigma / r)**12 - (sigma / r)**6) / r**2 # magnitude of force
        fij = f_mag * rij # force vector
        forces[i] += fij
        forces[j] -= fij # Newton's third law

  return forces

def velocity_verlet(positions, velocities, forces, dt, L):
  #update positions and velocities
  positions += velocities * dt + 0.5 * forces * dt**2
  positions %= L # apply periodic boundary conditions

  new_forces = compute_forces(positions, L)
  velocities += 0.5 * (forces + new_forces) * dt
  
  return positions, velocities, forces

def compute_kinetic_energy(velocities):
  return 0.5 * np.sum(velocities**2) # mass assumed as 1

def compute_temperature(velocities): #total kinetic energy = 3/2 * N * k_B where k_B (boltzmann constant) reduced to 1
  return (2.0 / 3.0) * compute_kinetic_energy(velocities) / N
