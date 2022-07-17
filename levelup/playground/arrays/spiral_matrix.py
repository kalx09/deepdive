class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        top = 0
        bottom = len(A) - 1
        right = len(A[0]) - 1
        left = 0

        dir = 0
        list_obj = []
        while top <= bottom and left <= right:

            if dir == 0:  # left to right
                for i in range(left, right + 1):  # (0, 4)
                    print(matrix[top][i], end=" ")
                    list_obj.append(matrix[top][i])
                    top += 1
                    dir = 1

            elif dir == 1:  # top to bottom
                for i in range(top, bottom + 1):  # (1, 4)
                    print(matrix[i][right], end=" ")
                    list_obj.append(matrix[i][right])
                    right -= 1
                    dir = 2

            elif dir == 2:  # right to left
                for i in range(right, left - 1, -1):  # (3, 0)
                    print(matrix[bottom][i], end=" ")
                    list_obj.append(matrix[bottom][i])
                    dir = 3
                    bottom -= 1

            elif dir == 3:  # bottom to top
                for i in range(bottom, top - 1, -1):  # (2, 0)
                    print(matrix[i][left], end=" ")
                    list_obj.append(matrix[i][left])
                    left += 1
                    dir = 0
        return list_obj


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

print(Solution().spiralOrder(matrix))
