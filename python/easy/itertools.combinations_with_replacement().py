from itertools import combinations_with_replacement

S, k = input().split()
k = int(k)

S = sorted(S)
perms = (combinations_with_replacement(S, k))
for perm in perms:
  print(''.join(perm))
