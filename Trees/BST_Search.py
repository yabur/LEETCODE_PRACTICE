class TreeNode:

    def __init__(self, key, left=None, right=None):
        self.key = key
        #self.value = value
        self.left = None  # can be called recursively TreeNode left;
        self.right = None # TreeNode right;
        
    # Time Complexity = O(logn)
    def search(self, root, k):
        """ Searching "k" key value in BST.

        Args:
            root (int): Pointer, reference to root of the Binary Search Tree
            k (int): Key value
            curr : current pointer
        """
        if root is None:
            return root
        curr = root
        
        while curr is not None:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None


    # Balance Tree, O(height) = O(logn)
    def insert(self, root, k):
            """ Insert new Key to the BST.
            
            Args:
                root (int): Pointer, reference to root of the Binary Search Tree
                k (int): Key
            """
            
            # Create new node to insert containing "k" key
            newNode =  TreeNode(k)

            if root is None:
                return newNode
            # Search the place to insert new key
            prev = None
            curr = root
            while curr is not None:
                if k == curr.key:
                    print("KEY already exists")
                elif k < curr.key:
                    prev = curr
                    curr = curr.left
                else:
                    prev = curr
                    curr = curr.right
                # curr = newNode  - CANT WORK BECAUSE IT DOES NOT HAVE ANY LINK.

                if  k < prev.key:
                    prev.left = newNode
                else:
                    prev.right = newNode
                return root
            
            
     # Balance Tree, O(height) = O(logn) , NOT Possible in hash table  O(n)
    def findMin(self, root):
        """ Find Min Value of BST tree 

        Args:
            root (int): root key

        Returns:
            curr.key: return min value containing by the key
        """
        if root is None:
            return None
        curr = root
        
        while curr.left is not None:
            curr = curr.left
        return curr.key
    
      # Balance Tree, O(height) = O(logn)
    def findMax(self, root):
        """ Find Max Value of BST tree 

        Args:
            root (int): root key

        Returns:
            curr.key: return max value containing by the key
        """
        if root is None:
            return None
        curr = root
        
        while curr.right is not None:
            curr = curr.right
        return curr.key
    
    
     # O(height) = O(logn)
    def successNode(self, root, p):
        """

        Args:
            root (int): root key
            p (int): next max value of the key
            
            Returns:
                curr (): reference to successor
                ancenstor(): reference to successor
        """
        
        if root is None:
            return None
        if p is not None:
            curr = p.right
            while curr.left is not None:
                curr = curr.left
            return curr
        
        # Search for p, starting from root
        
        ancestor = None
        curr = root
        while curr.key is not p.key:
            if p.key < curr.key:
                ancestor = curr # 
                curr = curr.left
            else:
                curr = curr.right
        return ancestor  # 
             
             
    # Cannot know if the the node that wanted to be delete is exists in the tree 
    # O(logn)   - Balance Tree
    def deleteNode(self, root, key):
        
        curr = root
        prev = None
        
        # curr is NONE.
        if curr is None:
            return root
        
        # first find the node 
        while curr is not None:
            if key == curr.key:
                break
            elif key < curr.key:
                prev = curr
                curr = curr.left
            else: # key > curr.key
                prev = curr
                curr = curr.right
                

            
        # case 1: Node is a leaf 
            if curr.left is None and curr.right is None:
                # check if curr is left or right child of the prev node to break the link 
                
                # Edge Case
                if prev is None: # one-node tree
                    return None
            if  curr is prev.left:
                prev.left = None
            else: # curr is prev.right
                prev.right = None
            return root
        
        # case 2: Curr node has one child
            
            if curr.left is None and curr.right is not None:
                child = curr.right
            if curr.left is not None and curr.right is None:
                child = curr.left
            
             # if root is the curr (edge case) no prev.
                if prev is None:
                    root = child
                return root
             
            if child is not None:
            
                if curr is prev.left:
                    prev.left = child
                else: # curr is prev.right
                    prev.right = child
                return root
            
        # Case 3: curr node has 2 child
            if curr.left is not None and curr.right is not None:
                curr.right is not None
                prev = curr
                succ = curr.right
                
                while succ.left is not None:
                    prev = succ
                    succ = succ.left
                    
                curr.key = succ.key
                
                if succ is prev.left:
                    prev.left = succ.right
                else: # succ is prev.right    
                    prev.right = succ.right
            return root
            
        
if __name__ == '__main__':
    #root = [3,9,20,None,None,15,7] 
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    print(root.findMin(root))