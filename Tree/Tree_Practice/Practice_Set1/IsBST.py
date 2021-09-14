# Is It A BST

# Given a binary tree, check if it is a binary search tree (BST). A valid BST does not have to be complete or balanced.

# Consider the below definition of a BST:

#     1- All nodes values of left subtree are less than or equal to parent node value
#     2- All nodes values of right subtree are greater than or equal to parent node value
#     3- Both left subtree and right subtree must be a BST
#     4- By definition, NULL tree is a BST
#     5- By definition, trees having a single node or leaf nodes are BST.


class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

# complete the function below


def isBST(root, l = None, r = None):
    # if tree is empty return t
    if root is None:
        return True

    if l != None:
        if l.val >= root.val:
            return False
                
    if r != None:
        if r.val < root.val:
            return False
    
    return isBST(root.left_ptr, l, root) and isBST(root.right_ptr,root,r)     
   

if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left_ptr = TreeNode(2)
    root.right_ptr = TreeNode(5)
    root.right_ptr.left_ptr = TreeNode(1)
    root.right_ptr.right_ptr = TreeNode(4)
    #root.right_ptr.left_ptr = TreeNode(25)
    #root.right_ptr.right_ptr = TreeNode(35)
      
    
    print(isBST(root))    
                
                     
    

    
