def find_two_sum(A, target_sum):
    for i in range(len(A)):
        sum_so_far = 0  
        for j in range(i, len(A)):
            sum_so_far += A[j]
            if sum_so_far == target_sum:
                print(A[i:j+1])


print(find_two_sum([ 10, 2, -2, -20, 10 ], -10))
# print(find_two_sum([4,1,3,2,9],12))
