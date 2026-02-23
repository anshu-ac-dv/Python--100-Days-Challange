from array import*

# Create an array of integers
arr1 = array('i', [1, 2, 3, 4, 5])
for i in range(len(arr1)):
    print(arr1[i], end=' ')

# Delete an element at index 2
del arr1[2]
print("After deleting:", arr1)

#
arr1.remove(2)
print("After removing 2:", arr1)