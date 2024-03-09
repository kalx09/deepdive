def findJudge(n, trust):
    trust_count = [0] * (n + 1)  # Initialize an array to count the number of trusts for each person

    for a, b in trust:
        trust_count[a] -= 1  # Person 'a' trusts someone
        trust_count[b] += 1  # Person 'b' is trusted by someone

    for i in range(1, n + 1):
        if trust_count[i] == n - 1:  # Check if person 'i' is trusted by everyone except themselves
            return i

    return -1  # Return -1 if no town judge is found

# Example usage
n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
print(findJudge(n, trust))  # Output: 3
