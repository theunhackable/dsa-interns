

n,e = 5, 5

edges = [(0, 1), (1, 2), (2, 4), (4, 3), (2, 3)]

# Adjacency matrix
'''
-> init a matrix of size n*n mark all values as 0
-> for every edge(u, v) place matrix[u][v] = 1; matrix[v][u] = 1
'''
adj_mat = [[0] * n for _ in range(n)]
print(adj_mat)


for (u, v) in edges:
  adj_mat[u][v] = 1
  adj_mat[v][u] = 1

print('adjacency matrix:')
for row in adj_mat:
  print(row)


# n -> number of nodes
# e -> number of edges
#Adjacency list
'''
-> init a list of length n where each value is another list which is empty
for every edge (u, v) list[u].append)(v); list[v].append(u);
'''

adj_list = [[] for _ in range(n)]

for (u, v) in edges:
  adj_list[u].append(v)
  adj_list[v].append(u)

print(adj_list)