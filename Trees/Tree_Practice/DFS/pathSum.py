
'''
    Complete the function below.
    The function accepts a TREENODE and an INTEGER as inputs and is expected to return a 2D INTEGER ARRAY.
'''
class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

    def all_paths_sum_k(self, root, k):
        
        if root is None:
            return False
        result = []
   
        def dfs(node, target, slate):
            slate.append(node.val)
            # Base Case: Leaf Node
            if node.left_ptr is None and node.right_ptr is None:
                if node.val == target:
                    result.append(slate[:])
            
            # Recursive Case: Internal nodes
            if node.left_ptr is not None: 
                dfs(node.left_ptr, target - node.val, slate)
            if node.right_ptr is not None:     
                dfs(node.right_ptr, target - node.val, slate)
            
            slate.pop()
                
                
        dfs(root, k, [])
        return result
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left_ptr = TreeNode(9)
    root.right_ptr = TreeNode(20)
    root.right_ptr.left_ptr = TreeNode(15)
    root.right_ptr.right_ptr = TreeNode(7)
    
    
    print(root.all_paths_sum_k(root, 30))
        
       
            