M = int(input())
numbers_a = input().split()
a = set()

for i in range(M):
    a.add(int(numbers_a[i]))    
    
N = int(input())
numbers_b = input().split()
b = set()

for i in range(N):
    b.add(int(numbers_b[i]))

final_set = a.symmetric_difference(b)

for value in sorted (final_set):
    print(value)
