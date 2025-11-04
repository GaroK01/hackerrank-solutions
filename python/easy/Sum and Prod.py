import numpy as np

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

np_matrix = np.array(matrix)
col_sums = np.sum(np_matrix, axis=0)

result = np.prod(col_sums)
print(result)
