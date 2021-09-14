# Right Side View Of A Binary Tree

# Given a binary tree, imagine yourself standing on the right side of it and return a list of the node labels that you can see from the top to the bottom. 
"""
    Complete the function below.
    The function accepts a TREENODE as input
    and is expected to return an INTEGER ARRAY.
"""

import collections

class TreeNode():
    def __init__(self, label=None, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right


    def right_view(self, root):

        if root is None:
            return []
        
        result = []
        q = collections.deque([root])
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
            result.append(temp[-1])
        return result

if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    
    print(root.right_view(root))
        