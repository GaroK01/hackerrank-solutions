# Get the total number of elements to add
n = int(input())

# Create the set
s = set()

# Add the elements of the set
for _ in range(n):
    s.add(input())

# Print the total number of elements
print(len(s))
