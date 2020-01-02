#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
def main():

  # Get the number of particles per cell
  number_particle_cell = get_number_particle_cell()

  # Get the number of cells
  number_cell = get_number_cell()

  # Set the number of grids
  number_grid = number_cell + 1

  # Get cell size
  cell_size = get_cell_size(number_cell)

  # Get grid coordinates
  grid_coordinate = get_grid_coordinate(number_grid, cell_size)

  # Get distribution
  distribution = get_distribution(number_particle_cell, \
                                  number_cell, \
                                  number_grid, \
                                  cell_size, \
                                  grid_coordinate)

  # Plot distribution
  plot_distribution(grid_coordinate, distribution)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get cell size
#------------------------------------------------------------------------------
def get_cell_size(number_cell):

  # Get cell size
  cell_size = 1.0 / float(number_cell)

  #Return
  return cell_size
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get distribution
#------------------------------------------------------------------------------
def get_distribution(number_particle_cell, \
                     number_cell, \
                     number_grid, \
                     cell_size, \
                     grid_coordinate):

  # Import
  from random import random

  # Format
  index        = [0] * 2
  length       = [0] * 2
  shape_factor = [0] * 2
  distribution = [0] * number_grid

  for counter in range(number_particle_cell * number_cell):
    # Get position of particle
    position = random()

    # Get index
    index[0] = int(position / cell_size)
    index[1] = index[0] + 1

    # Get length
    length[0] =   position - grid_coordinate[index[0]]
    length[1] = - position + grid_coordinate[index[1]]

    # Get shape factor
    shape_factor[0] = length[1] / cell_size
    shape_factor[1] = length[0] / cell_size

    # Add shape factor to distribution
    distribution[index[0]] += shape_factor[0]
    distribution[index[1]] += shape_factor[1]

  # Fix
  distribution[ 0] *= 2.0
  distribution[-1] *= 2.0

  # Return
  return distribution
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get grid coordinates
#------------------------------------------------------------------------------
def get_grid_coordinate(number_grid, cell_size):

  # Format
  grid_coordinate = []

  for counter in range(number_grid):
    # Get grid coordinates
    grid_coordinate.append(float(counter) * cell_size)

  # Return
  return grid_coordinate
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get the number of cells
#------------------------------------------------------------------------------
def get_number_cell():

  while True:
    # Input
    number_cell = input('The number of cells: ')

    # Convert
    number_cell = int(number_cell)

    # Check
    if (number_cell > 0):
      # Break
      break
    else:
      print('Invalid.')

  # Return
  return number_cell
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get the number of particles per cell
#------------------------------------------------------------------------------
def get_number_particle_cell():

  while True:
    # Input
    number_particle_cell = input('The number of particles per cell: ')

    # Convert
    number_particle_cell = int(number_particle_cell)

    # Check
    if (number_particle_cell > 0):
      # Break
      break
    else:
      print('Invalid.')

  # Return
  return number_particle_cell
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Plot distribution
#------------------------------------------------------------------------------
def plot_distribution(grid_coordinate, distribution):

  # Import
  import matplotlib.pyplot as plt
  from statistics import mean, stdev

  # Font
  plt.rcParams['font.family'] = 'FreeSans'

  # Get average
  average = mean(distribution)

  # Get standard deviation
  standard_deviation = stdev(distribution)

  # Make new window
  fig, ax = plt.subplots()

  # Plot
  plt.axhspan(average - standard_deviation, \
              average + standard_deviation, \
              alpha = 0.2, \
              label = 'Standard deviation', \
              color = 'gray')
  plt.axhline(average, color = 'orange', label = 'Average')
  plt.plot(grid_coordinate, distribution, '.-', label = 'Particle')

  # Set axes label
  ax.set_xlabel('Coordinate')
  ax.set_ylabel('The number of particles')

  # Set legend
  plt.legend()

  # Save figure
  plt.savefig('shape-factor-particle.pdf', bbox_inches = 'tight')

  # Close figure
  plt.close()
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Call main
#------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
#------------------------------------------------------------------------------
