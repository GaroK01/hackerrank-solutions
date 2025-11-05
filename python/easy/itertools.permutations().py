from itertools import permutations

S, k = input().split()
k = int(k)

perms = sorted(permutations(S, k))

for perm in perms:
  print(''.join(perm))
