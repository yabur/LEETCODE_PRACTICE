##
# Giving array which 2 element sum is target number.
##
# IN Sorted Array
# Use 2 pointer approach


# target = 10

def two_sum_sorted(A, target):
    """

    :param A:
    :param target:
    :return:
    """
    pointer1 = 0
    pointer2 = len(A) - 1

    while pointer1 < pointer2:
        summ = A[pointer1] + A[pointer2]

        if summ == target:

            return [pointer1, pointer2]

        elif summ < target:
            pointer1 += 1
        else:
            pointer2 -= 1

    return [-1, -1]


if __name__ == '__main__':
    A = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 8, 9, 9]
    print(two_sum_sorted(A, 80))
