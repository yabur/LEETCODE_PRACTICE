


def get_permutations(arr):
    result = []
    
    # Helper Function
    def helper(i, slate, result):
        # base case
        len_slate = len(slate)
        if (i == len_slate - 1 ):
            result.append(slate.copy())
            return
        else:
            for j in range (i, len_slate):
                slate[j] , slate[i] = slate[i], slate[j]
                print(f' {slate[j]} , {slate[i]} = {slate[i]}, {slate[j]}')
                helper(i+1, slate, result)
                slate[i], slate[j]  = slate[j], slate[i]            
    helper(0, arr.copy, result)
    return result

if __name__ == '__main__':
    arr = [1,2,3]
    print(get_permutations(arr))