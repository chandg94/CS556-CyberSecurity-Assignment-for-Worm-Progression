# Project 1
# Graphs for csv files

# import statements
import networkx as nx
import csv

nodes = [1000, 1500, 2000]
graphs = ['ErdosRenyi', 'BarabasiAlbert', 'WattsStrogatz']
for n in nodes:
    for g in graphs:
        G = nx.erdos_renyi_graph(n, 0.2)
        if(g == 'ErdosReyni'):
            G = nx.erdos_renyi_graph(n, 0.2)
        if(g == 'BarabasiAlbert'):
            G = nx.barabasi_albert_graph(n, 3)
        if(g == 'WattsStrogatz'):
            G = nx.watts_strogatz_graph(n, 4, 0.6)
        edge = G.edges()
        e = list(edge)
        name = str(g) + str(n)
        with open(name, 'w') as out:
            csv_out = csv.writer(out)
            for r in e:
                csv_out.writerow(r)
