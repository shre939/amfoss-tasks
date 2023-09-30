# Read the number of force vectors
n = int(input())

# Initialize variables for the sum of force vectors
sum_x = 0
sum_y = 0
sum_z = 0

# Read and process each force vector
for i in range(n):
    x, y, z = map(int, input().split())
    sum_x += x
    sum_y += y
    sum_z += z

# Check if the sum of force vectors equals (0, 0, 0)
if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else:
    print("NO")

