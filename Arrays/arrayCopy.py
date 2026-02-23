from array import*

a = array('i',[1,2,3,4,5])
print("Array elements are:")
for i in range(len(a)):
    print(a[i], end=' ')

# Copying array using array() method
copyArray = array(a.typecode, (x*3 for x in a))

# Copying array using slicing
# copyArray = a[:]
print("\nCopied array elements are:")
for i in range(len(a)):
    print(copyArray[i], end=' ')