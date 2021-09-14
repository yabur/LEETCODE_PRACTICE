"""
MergeSort(arr[],l,r)
if r > l
    1- Find the middle point to divide the array
    2- Call mergeSort for first half
    3- Call mergeSort for second half
    4- Merge the two halves sorted in step 2 and 3

"""


def mergeSort(arr):
    if len(arr) > 1:
        # Find the mid of the array
        mid = len(arr)// 2

        # Dividing the array elements to subarrays
        L = arr[:mid]
        R = arr[mid:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(R)

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first (L) subarray
        j = 0  # Initial index of second (R) subarray
        k = 0  # Initial index of merged subarray

        # compare 2 subarray element and put in array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # when run out of elements in either size put remaining elements to array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Print the array
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    arr = [6, 5, 12, 10, 9, 1]
    mergeSort(arr)

    print("Sorted array is: ")
    printList(arr)



#
# Complete the 'merge_sort' function below.
#
# The function accepts an integer array as parameter.
#
def merge_sort_helper(arr, start, end):
    if start >= end:
        return

    mid = int((end+start) / 2)

    merge_sort_helper(arr, start, mid)
    merge_sort_helper(arr, mid + 1, end)

    aux = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1

    while i <= mid:
        aux.append(arr[i])
        i += 1

    while j <= end:
        aux.append(arr[j])
        j += 1

    arr[start:end + 1] = aux

    return arr

def merge_sort(arr):
    if arr is not None and len(arr) > 1:
        return merge_sort_helper(arr, 0, len(arr) -1)
    else:
        return arr