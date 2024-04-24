# Import Statements
import random
import csv
import networkx as nx
import matplotlib.pyplot as plt
import sys
# Checking Length of Command Line Arguments
if len(sys.argv) < 4:
    print("Not Enough Arguments !")
    quit()
# Argument 1 - Name of file
name = sys.argv[1]
# Argument 2 - Probability with which to infect the node.
prob = float(sys.argv[2])
# Checking probability to see if between 0 and 1
if (prob >= 0 and prob <=1):
    pass
else:
    print("Wrong Probability! Probability must be between 0 and 1 !")
    quit()
# Argument 4 - The initial node to be infected with worm
InfNode = int(sys.argv[3])
# Open  csv file to extract edges
with open(name, 'r') as f:
    reader = csv.reader(f)
    edge = list(reader)
e = [[int(float(j)) for j in i] for i in edge]
# Creating graph using edges
Gr = nx.Graph()
Gr.add_edges_from(e)
# Set all nodes to not infected
nx.set_node_attributes(Gr, name = 'status', values = 'notinf')
# Infecting initial node to be infected
nx.set_node_attributes(Gr, name = 'status', values = {InfNode : 'isinf'})
time = 0
totalinf = []
roundinf = []
totalinfcnt = 0
while (1):
    infnodes = []
    for i in Gr.nodes():
        if Gr.nodes[i]['status'] == 'isinf':
            infnodes.append(i)

    infectedthisround = 0
    for n in infnodes:
        neighboursList = Gr.neighbors(n)
        for node in neighboursList:
            # If node is uninfected, then infect with prob.
            if (Gr.nodes[node]['status'] == 'notinf'):

                if (random.random() < prob):
                    # Infect node.
                    nx.set_node_attributes(Gr, name='status', values={node: 'isinf'})
                    totalinfcnt += 1
                    infectedthisround += 1
    time += 1
    totalinf.append(totalinfcnt)
    roundinf.append(infectedthisround)
    if (len(infnodes) == len(Gr)):
        break

print('Time for execution in number of rounds taken: ', time )
plt.plot(totalinf)
plt.title('Rate of Worm Spread for Network')
plt.xlabel('Number of Rounds')
plt.ylabel('Number of Infected Nodes')
plt.show()
plt.plot(roundinf)
plt.title('Rate of Worm Spread for Network')
plt.xlabel('Number of Rounds')
plt.ylabel('Number of Infected Nodes per Round')
plt.show()
