# Function to check for a winner in a single grid
def check_winner(grid):
    # Check rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != '.':
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != '.':
            return grid[0][i]
    
    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '.':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '.':
        return grid[0][2]

    return None

# Input the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Input the grid
    grid = [list(input().strip()) for _ in range(3)]

    # Check for a winner in the current grid
    winner = check_winner(grid)

    # Print the result for the current test case
    if winner:
        print(winner)
    else:
        print("DRAW")

