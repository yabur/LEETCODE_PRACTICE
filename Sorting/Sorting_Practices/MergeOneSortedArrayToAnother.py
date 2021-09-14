"""
Given two arrays:
1)  arr1 of size n, which contains n positive integers sorted in the ascending order.
2)  arr2 of size (2*n) (twice the size of first), which contains n positive integers sorted in the ascending order in its first half. Second half of this array arr2 is empty. (Empty elements are marked by 0).

Write a function that takes these two arrays, and merges the first one into second one, resulting in an increasingly sorted array of (2*n) positive integers.
Example
Input:
n = 3
arr1 = [1 3 5]
arr2 = [2 4 6 0 0 0]
Output: arr2 = [1 2 3 4 5 6]
"""


def merger_first_into_second(arr1, arr2):
    n = len(arr1)
    i = n - 1
    j = n - 1
    k = (2 * n) - 1

    while i >= 0 and j >= 0:
        if arr1[i] >= arr2[j]:
            arr2[k] = arr1[i]
            k -= 1
            i -= 1
        else:
            arr2[k] = arr2[j]
            k -= 1
            j -= 1

    while i >= 0:
        arr2[k] = arr1[i]
        k -= 1
        i -= 1

    # while j >= 0:
    #     arr2[k] = arr2[j]
    #     k -= 1
    #     j -= 1


# Driver program
if __name__ == '__main__':
    arr1 = [1, 3, 5, 0, 0, 0]
    arr2 = [2, 4, 6]

    merger_first_into_second(arr1, arr2)
    print(arr1)
