import collections

#class Graph:
    
def BFS (graph, source):
    
    visited = []
    captured = [] # 0 or 1
    parent = []
    q = collections.deque([source])
    
    while q is not None:
        v = q.pop()
        captured[v] = 1
        # look adjlist of popped v vertex.
        for w Adjlist[v]:
            # check if it is discovered
            if visited[w] == 0:
                visited[w] == 1
                parent[w] == v
                q.push(w) 
        
        
    
    
    