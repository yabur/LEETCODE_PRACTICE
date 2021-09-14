 # 108. Convert Sorted Array to BST
 # 
 # 
 # #
  
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sortedArrayToBST(self,val):

    def helper(A, start, end):
        if start > end:
            return None
        elif start == end:
            return TreeNode(A[start])
        else:
            mid = start + (end - start)//2
            
            subtreeroot = TreeNode(A[mid])
            subtreeroot.left = helper(A, start, mid-1)
            subtreeroot.right = helper(A, mid+1, end)
            
            return subtreeroot

    return helper(val,0, len(val)-1)                   