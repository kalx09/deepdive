
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if len(A) == 1:
            return str(A[0])
        A = [A[i] for i in range(len(A))]
        for x in range(len(A)):
            for y in range(1 + x, len(A)):
                if str(A[x]) + str(A[y]) < str(A[y]) + str(A[x]):
                    A[x], A[y] = A[y], A[x]
        result = "".join(map(str, A))
        if (result == '0' * len(result)):
            return '0'
        else:
            return result


print(Solution().largestNumber([8, 89]))
