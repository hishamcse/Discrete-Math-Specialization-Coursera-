import networkx as nx
from itertools import permutations


# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.

def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    # Write your code here.
    s = 0
    for i in range(len(cycle) - 1):
        s = s + g[cycle[i]][cycle[i + 1]]['weight']

    return s + g[cycle[len(cycle) - 1]][cycle[0]]['weight']


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Iterate through all permutations of n vertices
    min = 0
    for p in permutations(range(n)):
        m = cycle_length(g, p)
        if min == 0 or m < min:
            min = m
        # Write your code here.

    return min


g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight=2)
# We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=2)
g.add_edge(3, 0, weight=2)
g.add_edge(0, 2, weight=1)
g.add_edge(1, 3, weight=1)
