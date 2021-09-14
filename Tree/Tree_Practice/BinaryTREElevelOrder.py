# 
# 102. Binary Tree Level ORder Traversal
#    Given the root of a binary tree, return the level order 
#    traversal of its nodes' values. (i.e., from left to right, level by level).
# Ex : Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
# Time Complexity: O(n) bcz u visit all element once 
# Space Complexity: O(n) 
import collections

# Definition for a binary tree node.
class TreeNode:
     # Node Constructor 
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

     def levelOrders(self, root):
        """[summary]

        Args:
            root (TreeNodes): 
        Returns:
            List[List[int]]
        """
        
        # Special Case
        if root is None:
            return []
        
        result = []
        
        q = collections.deque([root])
       
        
        while len(q) != 0:  # while the queue is not empty
            numnodes = len(q) # find out how many nodes are in the current level
            tempnodes = [] # Save  
            for _ in range(numnodes): # Have to pop those many nodes. Note that new nodes in the next level will get pushed at the end
                node = q.popleft() 
                tempnodes.append(node.val) # temp array stores all the values in the current level
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            result.append(tempnodes) # take all the collected values and append to the result array
        return result
                
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    
    print(root.levelOrders(root))
        