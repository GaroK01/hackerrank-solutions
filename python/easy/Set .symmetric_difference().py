n_en = int(input())
s_en = set(input().split())

n_fr = int(input())
s_fr = set(input().split())


# Print the symmetric_difference (all non common elements) of the two sets
print(len(s_en.symmetric_difference(s_fr)))
