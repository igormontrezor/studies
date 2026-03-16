'''import numpy


def arrays(arr):
    a = numpy.array(arr)
    b = numpy.array([])
    for n in range(len(a), 0, -1):
        b = numpy.append(b, float(a[n-1]))
    return b
#arr = input().strip().split(' ')
arr = [1, 2, 3, 4, 5]
result = arrays(arr)
print(result)'''

'''import numpy



def arrays(arr):
    change_array = numpy.array(arr, int)
    return change_array

#arr = input().strip().split(' ')
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = arrays(arr)
print(result.reshape(3, 3))'''



import numpy

n,m = map(int,input().split(' '))
arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
print(numpy.transpose(arr))
arr_flat = numpy.array(arr)
print(arr_flat.flatten())
