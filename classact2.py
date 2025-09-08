import math
import copy
from math import sqrt
for i in range(2, 42, 2):
    print(i)

even = [2, 3, 4, "apple", 1.0]
print(even[3])
even[3] = "orange"
print(even[3])

even2 = [2, 3, 4, 5]
for val in range(len(even2)):
    even2[val] += 1
print(even2)

even3 = [[2, 3, 4], [3, 5, 6], [3, 4, 5]]
print(even3[1][1])

even3.insert([0][0], 40)
print(even3)

even4 = [2, 3, 4]
even5 = even4[:]
even4.pop(0)
even4.remove(3)
print(even5)

num = [x for x in range(10) if x%2 != 0]
print(num)

matrix = [[2, 3, 4], [30, 40, 50], [23, 23, 45]]
def add_one(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1

print(matrix)
add_one(matrix)
print(matrix)

matrix.copy()
#shallow copy -> copy.copy()
#deep copy -> copy.deepcopy()
