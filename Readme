# General

This file contains instructions to execute the Simulation
There are three files:
1. GraphGen.py : This file generates csv files for three different networks does not take any arguments
2. WormPropagationWithoutCure.py : 	This file simulates propagation without cure.
					This file takes 3 arguments and must have three arguments with proper values
3. WormPropagationWithCure.py : 	This file simulates propagation with cure.
					This file takes 5 arguments and must have five arguments with proper values
				
# Usage

First run the GraphGen.py file without any arguments to generate networks
and store them in csv files. 

Open a terminal:
$python3 GraphGen.py

The name for the files are <Network name><nodes>
Eg: ErdosRenyi1000
The name of the three networks (in the format to put) : ErdosRenyi, BarabasiAlbert, WattsStrogatz
The number of nodes are : 1000, 1500, 2000

To simulate Worm propagation without cure run:
$ python3 WormPropagationWithoutCure <network file name> <probability of infection> <initial infected node>
Eg:$ python3 WormPropagationWithoutCure ErdosRenyi1000 0.01 1
This generates two plots one after the other showing infection per unit time and total infections over time

To simulate Worm propagation with cure run:
$ python3 WormPropagationWithCure <network file name> <probability of infection> <initial infected node> <probability of cure> <initial cured node>
Eg:$ python3 WormPropagationWithCure ErdosRenyi1000 0.01 1 0.01 2
This generates one plot showing total infections over time.
