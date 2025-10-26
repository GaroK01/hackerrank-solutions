n_en = int(input())
set_en = set(input().split())

n_fr = int(input())
set_fr = set(input().split())

# Print the intersection (common elements) between the two sets
print(len(set_fr.intersection(set_en)))
