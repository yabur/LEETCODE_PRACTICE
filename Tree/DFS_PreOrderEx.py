# PreOrder Example 
    # 144. Binary Tree Preorder Traversal
        # Given a binary tree, return the preorder traversal or its nodes' values.
        # Input : [1,null,2,3]
        # Output : [1,2,3]
        # #
        
class TreeNode:
     # Node Constructor 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def preorderTraversal(self, root):
        """Pre order Traversal of a Tree

        Args:
            root (int): TreeNode

        Returns:
            List[int]
        """
        
        if root is None:
            return None
            
        result = []
        
        def dfs(node):
            
            # Base Case : Leaf Node.
            if node.left is None and node.right is None:
                result.append(node.val)
                return 
            
            # Recursive case: Internal node
            
            # Preorder processing
            result.append(node.val)
            
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
                
        dfs(root)
        return result
    
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    
    print(root.preorderTraversal(root))