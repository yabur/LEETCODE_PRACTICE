# How many binary search tree with n nodes?
#
#
# Recursive solution
# Catalen numbers = C(n) = 2n!/(n+1)n! 


def how_many_BSTs(n):
   
    def helper(node, C):
        # base case
        if node in C:
            return C[node]
        
        if node == 0 or node == 1:
            C[node] = 1
            return 1

        result = 0
        for i in range(0,node):
            result += helper(i, C) * helper(node - i - 1, C)
        C[node] = result
        return result

    return helper(n, dict())

#
# Dynamicly 
#
#

def howmany_BSTs(n):
    C = {}
    C[0] = C[1] = 1

    for i in range(2, n+1):
        C[i] = 0 # garbage value 
        for j in range(0,i):
            C[i] += C[j] * C[j-i-1]
    return C[n]

# Binomial Coeff.
# Better! O(n)

    
if __name__ == '__main__':
    res = how_many_BSTs(3)
    print(res)


