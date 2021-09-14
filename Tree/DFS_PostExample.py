class TreeNode:
    
    def __init__(self):
        """ Constructor
        
        Args:
            name (string)
            space (int)
        """
        self.name = name 
        self.space = space
        List = [] # child
        
    # PostOrder Example 
    # Amount of disk usage node uses
    #
        
    def helper(self, node):
        
        if node not in self:
            return 0
        du = node.space() # pre order initilazing 
        
        for child in node.children:
           du = du + helper(child)
        return du # post order result
        
        
if __name__ == '__main__':
    L = [5,6,3,67,89,4]
    newBook = TreeNode.dfs(L, 3)
    print(newBook)
    