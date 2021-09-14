import collections

'''
429. N-ary Tree Level Order Traversal
    
    Complete the function below.
    The function accepts a TREENODE as input
    and is expected to return a TWO-DIMENSIONAL LIST OF INTEGERS.
'''
class TreeNode:
    def __init__(self, _label):
        self.label = _label
        self.children = []

def level_order(root):
    
    # special class
    if root is None:
        return []
    
    result = []
    
    q = collections.deque([root])
    
    while len(q) != 0:
        numnodes = len(q)
        temp = []
        
        for n in range (0, numnodes):
            node = q.popleft()
            for child in node.children:
                q.append(child)
            temp.append(node.label)
        result.append(temp)
    return result
            
            
