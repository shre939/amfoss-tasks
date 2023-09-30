# Input the word typed by Alex
s = input()

# Define the word "hello"
hello = "hello"

# Initialize pointers for both strings
s_ptr = 0
hello_ptr = 0

# Iterate through the input string s
while s_ptr < len(s) and hello_ptr < len(hello):
    # If the current characters match, move both pointers
    if s[s_ptr] == hello[hello_ptr]:
        s_ptr += 1
        hello_ptr += 1
    else:
        # If they don't match, move the s_ptr only
        s_ptr += 1

# If hello_ptr reached the end of "hello," Alex succeeded in saying "hello"
if hello_ptr == len(hello):
    print("YES")
else:
    print("NO")

