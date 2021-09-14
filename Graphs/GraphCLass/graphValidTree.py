"""
To be a tree need to be connected and has no cycles.
1. yes it is a graph problem 
2. yes, traversal to find cycles (cross/back edges)
3. looking at what kind of edge we are 
    differentiate between tree edges, tree edges in 
    reverse, and cross edges/back edges.
    
    parent array
    

coding it up:
    turn edgelist -> adj_list
    
    outer loop?
        yes, to make sure we only run one traversal
    base bfs or dfs
    
    incorporate extention of looking for cyclic edges

"""

def valid_tree(n, edges)

def bfs(node): 
    q = Queue()
    q,push(node)
    visited(node)