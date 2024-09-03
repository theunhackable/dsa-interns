from collections import deque
'''
1. Add the node which you want to visit first
2. while there is an element in queue:
    a) pop it out
    b) check if the poped out if visited[node] == false
        i) mark it as true.
        ii) add unvisited neighbours to the queue
        iii) print the popped node 

'''

adj_list = [[1,6,5], [0, 2], [1,3,4,8], [2, 4, 7], [2, 3], [0, 6], [0, 5], [3], [2]]

n = len(adj_list)
# visited array
visited = [False] * n

q = deque()

q.append(0)

while len(q):
  node = q.popleft()
  if visited[node] == False:
    visited[node] = True
    for neighbour in adj_list[node]:
      if visited[neighbour] == False:
        q.append(neighbour)
    print(node, end=" ")

