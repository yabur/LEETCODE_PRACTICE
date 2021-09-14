# 

# Given a binary tree, return all paths from root to leaf.
# Output: [[1, 2, 4], [1, 2, 5], [1, 3, 6], [1, 3, 7]]
class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

# complete the function below
# Input: root of the input tree
# Output: A list of integer lists denoting the node values of the paths of the tree


def allPathsOfABinaryTree(root):
    
    if root is None:
        return []
    dfs(root, [])
    return result 
result = []

def dfs(node, slate):
    slate.append(node.val)
    # Base Case: Leaf Node
    if node.left_ptr is None and node.right_ptr is None:
        result.append(slate[:])
    
    if node.left_ptr:
        dfs(node.left_ptr, slate)
    if node.right_ptr:
        dfs(node.right_ptr, slate)
        
    slate.pop()
    


        
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(1)
    root.left_ptr = TreeNode(2)
    root.right_ptr = TreeNode(3)
    root.left_ptr.left_ptr = TreeNode(4)
    root.left_ptr.right_ptr = TreeNode(5)
    root.right_ptr.left_ptr = TreeNode(6)
    root.right_ptr.right_ptr = TreeNode(7)
      
    
    print(allPathsOfABinaryTree(root))    
                
                 
