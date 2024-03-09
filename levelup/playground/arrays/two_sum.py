def find_two_sum(A, target_sum):
    for i in range(len(A)):
        sum_so_far = 0  
        for j in range(i, len(A)):
            sum_so_far += A[j]
            if sum_so_far == target_sum:
                print(A[i:j+1])


print(find_two_sum([ 10, 2, -2, -20, 10 ], -10))
# print(find_two_sum([4,1,3,2,9],12))

def find_two_sum(nums, target):
    num_dict = {}  # Create an empty dictionary to store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]  # Return the indices of the two numbers
        num_dict[num] = i  # Add the number and its index to the dictionary

    return None  # If no two numbers add up to the target, return None

# Example usage:
numbers = [10, 2, -2, -20, 10]
target_sum = -10

result = find_two_sum(numbers, target_sum)
if result:
    index1, index2 = result
    print(f"The two numbers at indices {index1} and {index2} add up to the target sum.")
    print(f"The numbers are: {numbers[index1]} and {numbers[index2]}")
else:
    print("No two numbers add up to the target sum.")
