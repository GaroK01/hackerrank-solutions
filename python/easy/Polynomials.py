import numpy

poly_list = list(map(float,input().split()))
x = int(input())

print (numpy.polyval(poly_list, x))
