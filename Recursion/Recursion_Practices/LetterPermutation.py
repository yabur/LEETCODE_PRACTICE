# Mutable
#

# initialize solution array
# initialize subproblem (size)
# initialize partial solution

# Root Manager

def lcp(input_str):
    result = []
    length_input = len(input_str)

    def lcp_helper(i, slate):
        # Base Case
        if i == length_input:
            result.append("".join(slate))  # put into the empty list. (going back up)
            return

        # Recursive case
        if input_str[i].isdigit():
            slate.append(input_str[i])
            # create a child
            lcp_helper(i + 1, slate)
            slate.pop()
        else:
            slate.append(input_str[i].lower())
            # create a child
            lcp_helper(i + 1, slate)
            slate.pop()

            slate.append(input_str[i].upper())
            # create a child
            lcp_helper(i + 1, slate)
            slate.pop()

    lcp_helper(0, [])
    return result

if __name__ == '__main__':
    input_str = "a1b2"
    print(lcp(input_str))
