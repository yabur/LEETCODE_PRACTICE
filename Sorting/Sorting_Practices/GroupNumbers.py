# Group the Numbers
# Partitioning : quicksort !!
# Time - O(n), Space- O(1)
# Lomuto's partitioning O(n) time, in-place


def solve(arr):
    even = -1  # index from the beginning (r -- red == even)
    i = 0  # current pointer

    while i < len(arr):  # O(n)
        if arr[i] % 2 == 0:
            even += 1
            arr[i], arr[even] = arr[even], arr[i]
        i += 1
    return arr


if __name__ == '__main__':
    arr = [1, 5, 2, 3, 4, 4, 4, 5, 2, 6, 8, 9, 9]
def solve(arr):
    left_pointer = -1
    current_pointer = 0

    while current_pointer < len(arr) - 1:
        if (arr[current_pointer] % 2 == 0):
            left_pointer += 1
            arr[current_pointer], arr[left_pointer] = arr[left_pointer], arr[current_pointer]
        current_pointer += 1
    return arr