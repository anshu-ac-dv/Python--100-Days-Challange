import array
from array import*

var = array('d', [1, 2, 3, 4, 5])

for i in range(0, len(var)):
    print(var[i], end=' ')
    
print("\n")

print("Array elements using for loop:")

for x in var:
    print(x, end=',')