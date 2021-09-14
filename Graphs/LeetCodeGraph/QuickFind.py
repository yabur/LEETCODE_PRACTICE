class UnionFind:
    def  __init__ (self, size): 
        # initilize an array with values of its indexices
        
        self.root = [i for i in range(size)]
    
    # find x will give you its root value   O(1)
    def find(self, x):   
        return self.root[x]
    
    # O(N)
    def union(self, x, y):
        # first find x and y 
        rootX = self.find(x)
        rootY = self.find(y)
        #check if they are already connected
        if rootX != rootY:
            for i in range(len(self.root)): # traverse whole array to find 
                if self.root[i] == rootY:
                    self.root[i] = rootX
    # O(1)
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    
# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true    