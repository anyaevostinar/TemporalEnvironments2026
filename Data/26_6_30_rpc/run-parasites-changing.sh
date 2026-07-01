#!/bin/bash --login

## This file runs one experimental condition (i.e. a group of jobs
## that are the same except for their random seed)

## Email settings (they don't work for our setup)
#SBATCH --mail-type=ALL
#SBATCH --mail-user=does_not_work@carleton.edu

## Job name settings (These do matter, so UPDATE THEM)
#SBATCH --job-name=rpc
#SBATCH -o rpc%A_%a.out

## Memory requirement in megabytes. You might need to make this bigger.
#SBATCH --mem-per-cpu=2000M

## Launch an array of jobs. This determines your random seeds
#SBATCH --array=100-129

#SBATCH --nodes=1

#SBATCH --ntasks-per-node=29

cd /Accounts/caldwelll/TemporalEnvironments2026/Data/26_6_30_rpc
mkdir run_parasites_changing
cd run_parasites_changing

mkdir ${SLURM_ARRAY_TASK_ID}
cd ${SLURM_ARRAY_TASK_ID}

cp /Accounts/caldwelll/TemporalEnvironments2026/Data/26_6_30_rpc/SymSettings.cfg .
cp /Accounts/caldwelll/TemporalEnvironments2026/Data/26_6_30_rpc/flat-reward-1-env.json .
cp /Accounts/caldwelll/TemporalEnvironments2026/SymbulationEmp/symbulation_sgp .

## THIS IS AN EXAMPLE, UPDATE TO CORRECT THINGS
args=" -START_MOI 1 -ENABLE_TEMP_CHANGING_ENVIRONMENT true -TEMP_CHANGING_ENVIRONMENT_ORG_TYPE plastic-both" ##changing env not enabled?
./symbulation_sgp $args -SEED ${SLURM_ARRAY_TASK_ID} > run.log

## Run with sbatch -p facultynode --nodelist=edmonstone2024,margulis2024,carver,lederberg run-parasites-changing.sh