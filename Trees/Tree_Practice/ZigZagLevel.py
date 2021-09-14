import collections

"""
    Complete this function.
    The function accepts a TREENODE as input
    and is expected to return a two-dimensional INTEGER ARRAY.
"""


class TreeNode():
    def __init__(self, label=None, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right


    def zigzag_level_order_traversal(self, root):
        
        if root is None:
            return []
        
        result = []
        
        q = collections.deque([root])
        ltor = True
        while len(q) > 0:
            numnodes = len(q)
            temp = []
            
            for n in range(numnodes):
                node = q.popleft()
                temp.append(node.label)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if not ltor:
                temp.reverse()
            ltor = not ltor
            result.append(temp)
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    
    print(root.zigzag_level_order_traversal(root))
        
            
    
    