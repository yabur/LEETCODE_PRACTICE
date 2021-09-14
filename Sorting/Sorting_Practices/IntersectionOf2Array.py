#
# 2 pointer approach
# SORTED ARRAYS
#


def intersection(A1, A2):
    # A1.sort()
    # A2.sort()
    i = j = 0
    aux = []
    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            i += 1
        elif A1[i] > A2[j]:
            j += 1
        else:  # A1[i] == A2[j]
            if len(aux) == 0 or aux[len(aux) - 1] != A1[i]:
                aux.append(A1[i])
            i += 1
            j += 1
    return aux


def intersection3(a1, a2, a3):
    i = j = k = 0
    aux = []


if __name__ == '__main__':
    A1 = [2, 10, 3, 5, 5, 6, 7, 7, 8, 12]
    A2 = [5, 5, 6, 8, 8, 9, 10, 10]

    print(intersection(A1, A2))
