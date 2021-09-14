# a = [5, 9, 1, 3]

def twoSumSorted(a, target):
    
    i = 0
    j = len(a) - 1
    
    while i < j:
        if a[i] + a[j] == target:
            return [i,j]
        elif a[i] + a[j] > target:
            j -= 1
        else:
            i += 1
    return [-1,-1]

a = [5, 9, 1, 3]
target = 7
print(twoSumSorted(a, ))        