n_en = int(input())
set_en = set(input().split())

n_fr = int(input())
set_fr = set(input().split())

# Print the difference (elements present in the first set only) between the two sets
print(len(set_en.difference(set_fr)))
