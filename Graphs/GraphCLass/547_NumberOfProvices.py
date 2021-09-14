# union find class
class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        # use a rank array to record the height of each vertex, i.e, the "rank" of eaach vertex.
        # The initial "rank" of each vertex is 1, beacuse each of them is 
        # a standalone vertex with no connection to other vertices#
        
        self.rank = [1] * size
        self.count = size
        
    # The find function here is the same as that in the disjoint set with path compression.
    def find (self, x):
        # check if it is the root.
        if x == self.root[x]:
            return x
        # keep searching till you find your root node. Change parent of x to root node value.
        self.root[x] = self.find(self.root[x]) 
        # return the value of the root node.
        return self.root[x] 
    
    # The union function with union by rank 
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        # compare the hight of the trees to choose highest root node. 
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.rank[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.rank[rootX] = rootY        
            else: # they are same so merging them will be increase the hight of the tree.
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
            
            
    def getCount(self):
        return self.count
    
class Solution:
    def findCircleNum(self, isConnected):
        if not isConnected or len(isConnected) == 0:
            return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        return uf.getCount()
        
                