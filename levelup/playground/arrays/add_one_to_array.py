def solution(A):
	a_join = "".join(map(str,A))
	a_join = str(int(a_join)+1)
	A = list(a_join)
	A = [int(i) for i in A]
	return A

print(solution([9,9,9]))