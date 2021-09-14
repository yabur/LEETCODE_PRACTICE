
'''

112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


    Complete the function below.
    The function accepts a TREENODE and an INTEGER as inputs
    and is expected to return a BOOLEAN.
'''

class TreeNode():
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def path_sum(self, root, sum):

    
        # Special Case
        if root is None:
            return
        flag = [False]
        # Top-down DFS -> Additional arguments
        def dfs(node, target):
            # Base Case: Check Leaf Node or not? 
            if node.left is None and node.right is None:
                if target == node.val: 
                    flag[0] = True
            
            # Recursive Case: Internal node
            if node.left is not None:
                dfs(node.left, target - node.val)
            if node.right is not None:
                dfs(node.right, target - node.val)
                
        dfs(root, sum)
        return flag[0]
    
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    
    print(root.path_sum(root, 30))
    
    
    '''
    BFS
    class TreeNode():
        def __init__(self, val=None, left_ptr=None, right_ptr=None):
            self.val = val
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr

    Complete the function below.
    The function accepts a TREENODE and an INTEGER as inputs
    and is expected to return a BOOLEAN.


def path_sum(root, k):
    if root is None:
        return False
        
    stack = [(root, root.val)]
    
    while stack:
        (node, total) = stack.pop()
        
        if node.left_ptr is None and node.right_ptr is None:
            if total == k:
                return True
                
            continue
        
        if node.left_ptr:
            stack.append((node.left_ptr, total + node.left_ptr.val))
            
        if node.right_ptr:
            stack.append((node.right_ptr, total + node.right_ptr.val))
            
    return False
    
    '''