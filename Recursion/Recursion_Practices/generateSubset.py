#import string
#print (list(string.ascii_lowercase))

def generate_all_subsets(s):

    result = []

    def helper(i, slate):
         # base case
         if i == len(s):
            result.append("".join(slate))
            return

        # exclude
         helper(i+1, slate)

        # include
         slate.append(s[i])
         helper(i+1, slate)
         slate.pop()


    #   # recurse after adding current and not adding current to so_far
    #     helper(i+1, slate + [s[i]])
    #     helper(i+1, slate)

    helper(0, [])
    return result

if __name__ == '__main__':
    s = "xy"
    print(generate_all_subsets(s))


    # def generate_all_subsets(s):
    # output = []

    # # recursive function to generate subsets
    # def _generate_all_subsets(so_far, idx):
    #     if idx == len(s):
    #         # Base case. We reached the end of the string.
    #         # Some characters were included into list so_far, others were not.
    #         # This combination/subset of characters is unique.
    #         # Let us convert this list of characters to a string, store it in the output.
    #         output.append(''.join(so_far))
    #         return

  

    # _generate_all_subsets([], 0)

    # return output
