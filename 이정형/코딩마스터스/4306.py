import sys

def DFS(graph, v, discovered):
    discovered[v] = True          
    for u in graph.adjList[v]:
        if not discovered[u]: 
            DFS(graph, u, discovered)