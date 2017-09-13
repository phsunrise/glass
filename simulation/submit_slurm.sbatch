#!/bin/bash

#################
#SBATCH --job-name=test
#SBATCH --output=test.out
#SBATCH --error=test.err
#SBATCH --time=1:00:00
#SBATCH --qos=normal
#SBATCH --partition=iric
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mail-type=END
#SBATCH --mail-user=phsun@stanford.edu
#################

#mpirun -np 16 python mpi_test.py 
#python atoms_amplitude_poly.py -d
python preproc_sphere_W.py
