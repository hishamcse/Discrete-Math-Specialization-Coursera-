# import networkx as nx
#
#
# def dp(G):
#     n = G.number_of_nodes
#     T = [[float("inf")] * (1 << n) for _ in range(n)]
#     T[0][1] = 0
#     for s in range(1 << n):
#         if sum(((s >> j) & 1) for j in range(n)) <= 1 or not (s & 1):
#             continue
#
#         for i in range(1, n):
#             if not ((s >> i) & 1):
#                 continue
#             for j in range(n):
#                 if j == i or not ((s >> j) & 1):
#                     continue
#
#                 T[i][s] = min(T[i][s], T[j][s ^ (1 << i)] + G[i][j]['weight'])
#
#     return min(T[i][(1 << n) - 1] + G[0][i]['weight'] for i in range(1, n))

print([[float("inf")]*(1<<19)])