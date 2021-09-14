
# 1- Handle an empty tree as a special case.

# 2- Initialize an empty result array

# 3- Create an empty queue and push the root of the tree into it.
# 4- While the queue is not empty:
#     Count how many nodes there are in the queue
#     Repeat that many times:
#         Pop the next node from the front of the queue 
#         Append it to the result
#         if it has a left child, push it into the back of the queue
#         if it has a right child, push it into the back of the queue
#


import collections

# Definition for a binary tree node.
class TreeNode:
    #  Node Constructor 
     def __init__(self, root, left=None, right=None):
        self.root = root
        self.val = val
        self.left = left
        self.right = right
       
     def BFS_Template(self, root):
        # Step 1 
        if root is None:
            return []
        # Step 2
        result = []
     
         # Step 3
        q = collections.deque([root])
         # Step 4
        while len(q) !=0:
            numnodes = len(q)
            temp = []
            for _ in range(numnodes):
                node = q.popleft()
            
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                temp.append(node.val)
            result.append(temp)
            
        return result
    
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    
    print(root.levelOrders(root))
        