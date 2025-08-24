# core simulation logic
import numpy as np

N = 100 # number of particles
L = 10.0 # box size
dt = 0.01 # time step
steps = 1000 # number of steps

def initialize_positions(N, L):
  return np.random.rand(N, 3) * L # randn(i, j) creates a matrix of i rows and j columns with random numbers between 0 and 1

def initialize_velocities(N):
  v = np.random.randn(N, 3) # randN is a random distribution (mean 0, std = 1)
  v = -= np.mean(v, axis = 0) # remove net momentum (calculate average velocity of all partices and subtract from every individual particles velocity)
  # removing net momentum removes initial artificial drift of molecules
  
  return v

def compute_forces(positions, L):
  #apply minimum image convention
  #compute pairwise forces using LJ potential
  return forces

def velocity_verlet(positions, velocities, forces, dt, L):
  #update positions and velocities
  return new_positions, new_velocities, new_forces

def compute_kinetic_energy(velocities):
  return 0.5 * np.sum(velocities**2) # mass assumed as 1

def compute_temperature(velocities): #total kinetic energy = 3/2 * N * k_B where k_B (boltzmann constant) reduced to 1
  return (2.0 / 3.0) * compute_kinetic_energy(velocities) / N
