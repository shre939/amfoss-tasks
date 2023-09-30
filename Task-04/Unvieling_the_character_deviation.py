# Function to calculate the number of differing indices
def differing_indices(s):
    reference = "amfoss"
    count = 0
    for i in range(len(s)):
        if s[i] != reference[i]:
            count += 1
    return count

# Input the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    s = input().strip()
    result = differing_indices(s)
    print(result)

