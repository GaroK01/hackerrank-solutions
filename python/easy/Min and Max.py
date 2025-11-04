n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

np_matrix = np.array(matrix)
min_matrix = np.min(np_matrix, axis=1)
max_matrix = np.max(min_matrix)

print(max_matrix)
