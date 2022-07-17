class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    pass


def spiralOrder(A):
    top = 0
    bottom = A - 1
    right = A - 1
    left = 0

    counter = 1
    list_obj = [[0 for x in range(A)] for x in range(A)]

    while True:
        if top > bottom:
            break

        for i in range(left, right + 1):  # (0, 4)
            list_obj[top][i] = counter
            counter += 1
        top += 1

        if left > right:
            break

        for i in range(top, bottom + 1):  # (1, 4)
            list_obj[i][right] = counter
            counter += 1
        right -= 1

        if top > bottom:
            break

        for i in range(right, left - 1, -1):  # (3, 0)
            list_obj[bottom][i] = counter
            counter += 1
        bottom -= 1

        if left > right:
            break

        for i in range(bottom, top - 1, -1):  # (2, 0)
            list_obj[i][left] = counter
            counter += 1
        left += 1

    return list_obj

print(spiralOrder(4))
