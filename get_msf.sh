#!/bin/bash
#$ -cwd
#$ -m abe
#$ -M researcher-a@university1.edu

echo "Starting job at `date`"
python get_msf.py &> get_msf.out
echo "Finished job at `date`"
