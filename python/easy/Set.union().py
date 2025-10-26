# Enter your code here. Read input from STDIN. Print output to STDOUT

n_en = int(input())
s_en = set(input().split())

n_fr = int(input())
s_fr = set(input().split())


# Print the union (all the elements) of the two sets
print(len(s_en.union(s_fr)))
