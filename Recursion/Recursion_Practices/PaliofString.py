


# Complete the function below.

def generate_palindromic_decompositions(s):
    resultMap = {}

    def is_palindrome(start, end):
        if s[start] != s[end]:
            return False
        if start >= end:
            return True
        return is_palindrome(start+1, end-1)
    
    for startIndex in range(len(s), -1 ,-1): #start index = 3
        inter = []
        for i in range(startIndex, len(s)):
            if is_palindrome(startIndex, i):
                if i == len(s) - 1:
                    inter.append(s[startIndex:])
                else:
                    prefix = s[startIndex:i + 1]
                    for p in resultMap[i+1]:
                        inter.append(prefix + "|" + p)
            resultMap[startIndex] = inter
    return resultMap[0]






# def partition( s: str):
#     res = []
    
#     def dfs(i, slate):
#         # base case
#         if i >= len(s):  
#             res.append(slate.copy())
#             return
#         for j in range(i,len(s)):
#             if isPali(s, i, j):
#                 #ipdb.set_trace()
#                 slate.append(s[i:j+1], end="|")
#                 dfs(j+1, slate)
#                 slate.pop()
#     dfs(0, [])
#     return res

# def isPali( s, l, r):
#     while l < r:
#         if s[l] != s[r]:
#             return False
#         l, r = l + 1 , r - 1
#     return True

if __name__ == '__main__':
    input_str = "abb"
    print(generate_palindromic_decompositions(input_str))
    