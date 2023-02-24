import matplotlib.pyplot as plt
import networkx as nx
import json
import re


def sorted_nicely(l):
    """ Sort the given iterable in the way that humans expect."""
    def convert(text): return int(text) if text.isdigit() else text

    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


G = nx.Graph()

data = json.load(open("matches.json"))
x = data["data"]

women = []

for i in x.values():
    women.append(i)
women = sorted_nicely(women)


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
