# Import
import random
import csv
import networkx as nx
import matplotlib.pyplot as plt
import sys
# Checking Length of Command Line Arguments
if (len(sys.argv)<6):
    print("Not Enough Arguments !")
    quit()
# Inputing arguments into variables
# Argument 1 - Name of file
name=sys.argv[1]
# Argument 2 - Probability of infection
probinf = float(sys.argv[2])
# Checking probability to see if between 0 and 1
if (probinf>=0 and probinf<=1):
    pass
else:
    print("Wrong Probability! Probability must be between 0 and 1 !")
    quit()
# Argument 3 - The initial node to be infected with worm
InfNode=int(sys.argv[3])

# Argument 4 - Probability with which to cure
probcure=float(sys.argv[4])
if (probcure>=0 and probcure<=1):
    pass
else:
    print("Wrong Probability! Probability must be between 0 and 1 !")
    quit()
# Argument 5- Initial node be cured.
CureNode=int(sys.argv[5])

# Open  csv file to extract edges
with open(name, 'r') as f:
    reader = csv.reader(f)
    edge = list(reader)

e=[[int(float(j)) for j in i] for i in edge]
# Creating graph using edges
Gr=nx.Graph()
Gr.add_edges_from(e)
# Set all nodes to not infected and not cured
nx.set_node_attributes(Gr, name='status', values='notinf')
nx.set_node_attributes(Gr, name='cured', values='no')
# Infecting initial node to be infected and curing initial node to be cured
nx.set_node_attributes(Gr, name='status', values={InfNode: 'isinf'})
nx.set_node_attributes(Gr, name='cured', values={CureNode: 'yes'})

time=0
totalinf=[]
totalcure=[]

while (True):
    curednodes=[]
    infnodes=[]
    # Get list of infected nodes.
    for n in Gr.nodes():
        if (Gr.nodes[n]['status']=='isinf'):
            infnodes.append(n)
    infectionCount=len(infnodes)

    # Get list of inoculated nodes.
    for n in Gr.nodes():
        if Gr.nodes[n]['cured']=='yes':
            curednodes.append(n)
    inoccount=len(curednodes)

    # Infecting
    for n in infnodes:
        neighboursList=Gr.neighbors(n)
        for node in neighboursList:
            if ((Gr.nodes[node]['status'] == 'notinf') and (Gr.nodes[node]['cured']=='no')):
                if (random.random()<probinf):
                    nx.set_node_attributes(Gr, name='status', values={node: 'isinf'})

    # Curing

    for n in curednodes:
        neighboursList = Gr.neighbors(n)
        for node in neighboursList:
            if (Gr.nodes[node]['cured']=='no'):
                if (random.random()<probcure):
                    nx.set_node_attributes(Gr, name='cured', values={node: 'yes'})
                    nx.set_node_attributes(Gr, name='status', values={node: 'notinf'})
                    inoccount += 1
    time += 1
    totalinf.append(infectionCount)
    totalcure.append(inoccount)
    if (len(curednodes) == len(Gr)):
        break

print('Time for execution in number of rounds taken: ', time )
plt.plot(totalinf)
plt.title('Rate of Worm Spread for Network with Cure Applied')
plt.xlabel('Round')
plt.ylabel('Number of Infected Nodes')
plt.show()




