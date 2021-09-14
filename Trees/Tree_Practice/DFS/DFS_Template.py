# Handle an empty tree as a special edge case
# General strategy executed by every node in the tree:
# function "TOP-DOWN" dfs(node):  
"""
TOP-DOWN dfs(node, information passed down by parent):
    # Process the information coming into the node
"""

    # Base Case: If the node is a leaf, do whatever needs to be done for a leaf
    
    # Recursive case: the node is an internal node
    # if the node has a left child, dfs(node.left)
    # if the node has a right child, dfs(node.right)
    
#

# Handle an empty tree as a special edge case
# General strategy executed by every node in the tree:
# function "BOTTOM-UP" dfs(node):

    # Base Case: If the node is a leaf, do whatever needs to be done for a leaf
        
        # Recursive case: the node is an internal node
        # if the node has a left child, R1 = dfs(node.left)
        # if the node has a right child, R2 = dfs(node.right)
        
    # Process information (R1 and R2) coming into the node 
    # Return information up to the parent
"""
BOTTOM-UP dfs(node, information passed down by parent):
    # Process the information coming into the node
"""
    
class TreeNode:
    def __init__(self,value):   
        self.left = None
        self.right = None
        self.value = value
  
    def dfs_template(self, root):
        # Special Case
        if root is None:
            return

        def dfs(self,node):
            # Base Case : Leaf Node
            if node.left is None and node.right is None:
                # Base case answer generated here

            # Recursive case: Internal node
             if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
                
        dfs(root)
        
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    
    print(root.levelOrders(root))
    
    
        
        
