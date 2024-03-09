class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        i, j, k = 0, 0, 0
        C = [None] * (m + n)

        while i < m and j < n:
            if A[i] < B[j]:
                C[k] = A[i]
                i += 1
            else:
                C[k] = B[j]
                j += 1
            k += 1

        while i < m:
            C[k] = A[i]
            i += 1
            k += 1

        while j < n:
            C[k] = B[j]
            j += 1
            k += 1

        c_len = len(C)
        if c_len % 2 != 0:
            return C[c_len // 2]
        else:
            mid_1 = (c_len // 2) - 1
            mid_2 = mid_1 + 1
            avg = float((C[mid_1]+C[mid_2])) / float(2)
            return avg


print(Solution().findMedianSortedArrays([0, 23], []))
