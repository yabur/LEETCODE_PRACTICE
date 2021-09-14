result = []

def get_permutations(arr):
    # Write your code here
    get_permutations_helper(0, arr.copy())
    return result
    
    
def get_permutations_helper(i, slate):
    if i == len(slate) - 1:
        result.append(slate.copy())
    else:
        for k in range(i, len(arr)):
            slate[k], slate[i] = slate[i], slate[k]
            get_permutations_helper(i+1, slate)
            slate[k], slate[i] = slate[i], slate[k]
            
if __name__ == '__main__':
    arr = [1,2,3]
    print(get_permutations(arr))

def get_permutations(arr):
# Write your code here

    def recursion(idx, arr):
        if idx == len(arr):
            return [[]]
        
        permute_after_idx = recursion(idx + 1, arr)
        permute_with_idx = []
        for permute_ in permute_after_idx:
            for i in range(len(permute_) + 1):
                permute_with_idx.append(permute_[:i] + [arr[idx]] + permute_[i:])
        return permute_with_idx

    return recursion(0, arr)

if __name__ == '__main__':
    arr = [1,2,3]
    print(get_permutations(arr))
