import networkx as nx


# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the average weight of a Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)


def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))

    # Write your code here.
    return (2 / (n - 1)) * sum_of_weights  # undirected graph,so,the formula for the directed graph will be doubled


g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight=2)
# We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=2)
g.add_edge(3, 0, weight=2)
g.add_edge(0, 2, weight=1)
g.add_edge(1, 3, weight=1)

print(average(g))
