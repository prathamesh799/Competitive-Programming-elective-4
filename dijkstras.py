# Write a program that finds the shortest path from a source 
# vertex (0) to all other vertices. Following is a sample 
# input and output files.

# Sample Input:
# 8
# 15
# 4 5 0.35
# 5 4 0.35
# 4 7 0.37
# 5 7 0.28
# 7 5 0.28
# 5 1 0.32
# 0 4 0.38
# 0 2 0.26
# 7 3 0.39
# 1 3 0.29
# 2 7 0.34
# 6 2 0.40
# 3 6 0.52
# 6 0 0.58
# 6 4 0.93

# Sample Output:
#  0 to 0 (0.00)  
#  0 to 1 (1.05)  0->4  0.38   4->5  0.35   5->1  0.32
#  0 to 2 (0.26)  0->2  0.26
#  0 to 3 (0.99)  0->2  0.26   2->7  0.34   7->3  0.39
#  0 to 4 (0.38)  0->4  0.38
#  0 to 5 (0.73)  0->4  0.38   4->5  0.35
#  0 to 6 (1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52
#  0 to 7 (0.60)  0->2  0.26   2->7  0.34

# class ShortestPaths:
#     # Your code goes here...

# Pleae go through the module resources which you can find in the week - 3 Day - 1
from heapq import heappop, heappush
import sys
class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight
class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight
 
 
class ShortestPaths:
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
        for edge in edges:
            self.adj[edge.source].append(edge)
 
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)

def findShortestPaths(graph, source, N):
    pq = []
    heappush(pq, Node(source, 0))
    dist = [sys.maxsize] * N
    dist[source] = 0
    done = [False] * N
    done[source] = True
    prev = [-1] * N
    route = []
    while pq:
        node = heappop(pq)      
        u = node.vertex         
        for edge in graph.adj[u]:
            # print(edge.dest,edge.source)
            myval = str(edge.source)+str(edge.dest)
            v = edge.dest
            weight = edge.weight
            mydict[myval] = weight
            # print(".....",weight)
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = round(dist[u] + weight,2)
                # print(dist[v])
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
        done[u] = True
    print(f"{source} to {source} ({round(0.00,2)})")
    for i in range(1, N):
        if i != source and dist[i] != sys.maxsize:
            get_route(prev, i, route)
            resstr = " "
            for j in range(1,len(route)):
                pv = mydict[str(route[j-1])+str(route[j])]
                resstr = resstr + str(route[j-1])+" -> "+str(route[j])+"  "+ str(pv)+"   "
            print(f"{source} to {i} ({dist[i]})  {resstr}")
            route.clear()
 
 
    # Your code goes here...
edges = [Edge(4,5,0.35), Edge(5,4,0.35), Edge(4, 7, 0.37),
            Edge(5, 7, 0.28), Edge(7, 5, 0.28), Edge(5, 1, 0.32),
            Edge(0,4,0.38), Edge(0,2,0.26), Edge(7,3,0.39),Edge(1,3,0.29),Edge(2,7,0.34),Edge(6,2,0.40),Edge(3,6,0.52),Edge(6,0,0.58),Edge(6,4,0.93)]
N = 8
mydict = {}
graph = ShortestPaths(edges, N)
source = 0
findShortestPaths(graph, source, N)