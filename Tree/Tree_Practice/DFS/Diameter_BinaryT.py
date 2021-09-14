
"""
 543. Diameter of Binary Tree
 
    Complete the function below.
    The function accepts a TREENODE as input
    and is expected to return an INTEGER.
"""
# Global problem: Find the diameter of the whole tree 
# Local(per node) problem: Find the longest inverted-v path through the node 
# Local -> Global: Global solution is the max of all the local solutions
# To get the local solution, each needs to know from its two subtrees what their heights are




# Start at the leftmost node
class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

        
    
    def binary_tree_diameter(self, root):
         
        if root is None:
            return 0
        
        diameter = []
        diameter.append(0)
      
            
        def dfs(node, diameter):
            #base case
            if node.left_ptr == None and node.right_ptr == None:
                pass
                
            
            #recursive case
            L = 0
            R = 0

            if node.left_ptr != None:
                L = 1+dfs(node.left_ptr, diameter)
                
            if node.right_ptr != None:
                R = 1+dfs(node.right_ptr, diameter)
                
            if L+R > diameter[0]:
                diameter[0] = L+R
                
            return max(L,R)
            
            
        dfs(root,diameter)
        return diameter [0]      
            
      
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left_ptr = TreeNode(9)
    root.right_ptr = TreeNode(20)
    root.right_ptr.left_ptr = TreeNode(15)
    root.right_ptr.right_ptr = TreeNode(7)
      
    
    print(root.binary_tree_diameter(root))