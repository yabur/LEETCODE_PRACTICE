def get_permutations(arr):
    # Write your code here
    result = []
    
    
    
    # Helper Function
    def helper(i, slate):
        # base case
       
        if i == len(slate)-1:
            result.append(slate.copy())
            return
        else:
            inarray = {}
           
            for j in range (i, len(slate)):
                 if slate[j] not in inarray:
                    inarray[slate[j]] = 1
                    slate[j] , slate[i] = slate[i], slate[j]
                    helper(i+1, slate)
                    slate[i], slate[j]  = slate[j], slate[i]            
    helper(0, arr.copy())
    return result


if __name__ == '__main__':
    arr = [1,2,2]
    print(get_permutations(arr))