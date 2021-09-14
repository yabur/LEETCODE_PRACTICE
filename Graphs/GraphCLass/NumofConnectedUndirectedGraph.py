# 323. Number of Connected Componetnts in Undirected Graph
# 
 # Space: 
 #  adj_list: n+m
 #  visited: n
 #  queue: n / call stack for dfs: n
 #  
 #  O(n+m)
 # 
 # Time:  
 #  build adj_list: m 
 # bfs/dfs +outer loop: n+m
 #
 # O(n+m)
 # 
 # #
    
import queue

def num_connected_components(n, edges: list):
    
    # do we need to build the graph?
    # edges -> adj_list
    
    adj_list = [[] for i in range(n)]
    
    """   
        0| [] 
        1| []
        2| []
        3| []
        4| []    
    """ 
    # create undirected edges.
    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)
        
    """   
        0| [1] 
        1| [0,2]
        2| [1]
        3| [4]
        4| [3]    
    """  
        
        
   # OUTER LOOP
        
    # create an array to keep track of visited nodes.
    # Initially -1 for all values.  
    visited = [-1] * n
    
    
    components = 0
    
    # if node not visited
    # This loop does not do all the dfs traversals 
    # only does it the nodes that are not visited.(outer loop)
    for i in  range(n):
        if visited[i] == -1:
            dfs(i, visited) or bfs(i, visited)
            components += 1

    
def bfs(node, visited):
    q = queue.Queue()
    q.push(node)
    # mark as visited
    visited[node] = 1
    
    while q is not empty:
        # get unvisited neighbors of q.pop, and add to queue, and 
        curr = q.pop()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = {}
        graph = self.Grapher(edges)
        visited = set()
        length = len(graph)
        count = 0
        
        if length !=n:
            count += abs(n-length)
        # count the number of connected components
        for key,value in graph.items():
            if key not in visited:
                self.DFS(graph,key,visited)
                count+=1
        return count
    
    # travese the graph
    def DFS(self,graph,src,visited):
        if src in visited:
            return
        visited.add(src)
        for neighbor in graph[src]:
            self.DFS(graph,neighbor,visited)
    
    # create an adjaceny list using the edges
    def Grapher(self,edges):
        graph = {}
        
        for key,value in edges:
            if key not in graph:
                graph[key] = []
            if value not in graph:
                graph[value] = []
                
            graph[key].append(value)
            graph[value].append(key)
            
            
        return graph
