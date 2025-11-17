import numpy

N = int(input())

A = []
for _ in range(N):
  row = list(map(int, input().split()))
  A.append(row)

A = numpy.array(A)

B = []
for _ in range(N):
  row = list(map(int, input().split()))
  B.append(row)

B = numpy.array(B)

matrix = numpy.dot(A, B)

print(matrix)
