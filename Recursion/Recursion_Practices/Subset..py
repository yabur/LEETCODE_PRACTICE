def subset(arr):
    result = []

    def helper(i, slate):
         # base case
         if i == len(s):
            result.append(list(slate))
            return

        # exclude
         helper(i+1, slate)

        # include
         slate.append(s[i])
         helper(i+1, slate)
         slate.pop()

    helper(0, [])
    return result
    

if __name__ == '__main__':
    s = [1,2,3]
    print(subset(s))
