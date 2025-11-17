import numpy

numpy.set_printoptions(legacy='1.13')

numpy_array = list(map(float, input().split()))

numpy_array = numpy.array(numpy_array)

print(numpy.floor(numpy_array))
print(numpy.ceil(numpy_array))
print(numpy.rint(numpy_array))
