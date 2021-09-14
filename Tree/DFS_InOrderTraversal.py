# In Order Example 
    # 94. Binary Tree Inorder Traversal
        # Given the root of a binary tree, return the inorder traversal of its nodes' values
        # Input: root = [1,null,2,3]
        # Output: [1,3,2]
    
  
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def InorderTraversal(self, root):
        # Special Case
        if root is None:
            return []
        
        result = []
        
        stack = [(root,None)]
        

        while len(stack) !=0:
            (node,zone) = stack[-1]
            
            if zone is None:
                stack[-1] = (node, "arrival")
                if node.left is not None:
                    stack.append((node.left, None))
            elif zone == "arrival":
                stack[-1] = (node, "interim")
                result.append(node.val)
                if node.right is not None:
                    stack.append((node.right, None))
            elif zone == "interim":
                stack[-1] = (node, "departure")
                stack.pop()
        return result



def inorder(root):
    
    result = []
    inorder_helper(node=root, result=result)
    return result

def inorder_helper(node, result):
    
    
    if node.left_ptr is None and node.right_ptr is None:
        pass
    
    if node.left_ptr is not None:
        inorder_helper(node.left_ptr, result)
        
    result.append(node.label)
    
    if node.right_ptr is not None:
        inorder_helper(node.right_ptr, result)



if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)    
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(root.InorderTraversal(root))