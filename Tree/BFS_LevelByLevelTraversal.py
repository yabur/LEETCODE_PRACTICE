import collections
class TreeNode:
    
    def __init__(self):
        self.key = key
        self.value = value
        list = []  # <TreeNode> children
        self.node = TreeNode
        #node 
        for child in node.children:
            print (child.key)
            
            
            # BFS O(n)  visits every node.
            def levelorder(root):
                """ Breadth-first search""" 

                q = collections.deque([root])
                q.push(root)
                while q is not None:
                    node = q.pop()
                    print(node)
                    
                    if node.left is not None:
                        q.push(node.left)
                    if node.right is not None:
                        q.push(node.right)
                        
                    # n array tree
                    if node.children is not None:
                        for child in node.children:
                            q.push(child)
                            
                            
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    
    print(root.preorderTraversal(root))