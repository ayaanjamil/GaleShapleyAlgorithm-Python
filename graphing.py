import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

x = {'man1': 'woman1', 'man2': 'woman4',
     'man3': 'woman2', 'man4': 'woman3', 'man5': 'woman5'}

women = []

for i in x.values():
    women.append(i)
women.sort()


positions = {}
p = 0
for i in x.keys():
    G.add_node(i)
    positions[i] = [0, p]
    p += 10

p = 0
for i in women:
    G.add_node(i)
    positions[i] = [1, p]
    p += 10

for i in x.keys():
    G.add_edge(i, x[i])


nx.draw(G, with_labels=True, pos=positions)
plt.show()
