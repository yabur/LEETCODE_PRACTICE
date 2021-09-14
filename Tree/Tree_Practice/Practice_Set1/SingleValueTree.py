class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

count = 0
def singlevaluehelper(node):
    global count
    # Base condition
    if node.left_ptr is None and node.right_ptr is None:
        count = count + 1
        return True
        
    left_tree, right_tree = True, True
    if node.left_ptr is not None: 
        left_tree = singlevaluehelper(node.left_ptr) and node.left_ptr.val == node.val
    if node.right_ptr is not None: 
        right_tree = singlevaluehelper(node.right_ptr) and node.right_ptr.val == node.val
    
    if left_tree and right_tree :
        count = count + 1
    return left_tree and right_tree
        
def findSingleValueTrees(root):
    # Edge case
    if root is None: return 0
    
    singlevaluehelper(root)
    
    return count

if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left_ptr = TreeNode(9)
    root.right_ptr = TreeNode(20)
    #root.left_ptr.left_ptr = TreeNode(15)
    #root.left_ptr.right_ptr = TreeNode(15)
    root.right_ptr.left_ptr = TreeNode(15)
    root.right_ptr.right_ptr = TreeNode(7)
      
    
    print(findSingleValueTrees(root)) 