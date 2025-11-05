from itertools import combinations

S, k = input().split()
S = sorted(S)
k = int(k)

for n in range(1, k + 1):
  for combi in combinations(S, n):
    print(''.join(combi))
