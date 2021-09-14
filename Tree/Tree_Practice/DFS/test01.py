

# Start at the leftmost node
class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

# def binary_tree_diameter(root):
#     diameter = [0]
    
#     def solve_df(node: TreeNode, diameter: list) ->int:
#         if node.left_ptr == None and node.right_ptr== None:
#             return 0
#         l = 0; r=0;
#         if node.left_ptr:
#             l = 1 + solve_df(node.left_ptr, diameter)
#         if node.right_ptr:
#             r = 1 + solve_df(node.right_ptr, diameter)
#         if l+r > diameter[0]:
#             diameter[0] = l+r
#         return l if l > r else r
        
#     solve_df(root,diameter)
#     return diameter[0]


def binary_tree_diameter(root):
    if root is None:
        return 0
    
    diameter = []
    diameter.append(0)
            
    dfs(root, diameter)
    return diameter[0]
    
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
    
    
    
# dia = 0
# def binary_tree_diameter(root):   
#     # dia = [0]
#     diaHelper(root)
#     return dia
    
# def diaHelper(node):
#     if not node:
#         return 0
        
#     leftHeight = diaHelper(node.left_ptr)
#     rightHeight = diaHelper(node.right_ptr)
    
#     localDia = leftHeight + rightHeight

    
#     global dia
#     dia = max(dia, localDia)

    
#     return 1 + max(leftHeight, rightHeight)

if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left_ptr = TreeNode(9)
    root.right_ptr = TreeNode(20)
    root.right_ptr.left_ptr = TreeNode(15)
    root.right_ptr.right_ptr = TreeNode(7)
      
    
    print(binary_tree_diameter(root))