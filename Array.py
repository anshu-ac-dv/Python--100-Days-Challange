from array import*

a = array('i', [1, 2, 3, 4, 5])
print(a)

print("\n")

print("Array elements are:")
for i in range(0,5):
    print(a[i], end=' ')

print("\n")

print("Array elements using for loop:")
for i in range(0,len(a)):
    print(a[i], end=' ')

print("\n")
print(a.typecode)

print("Array item size is:", a.itemsize)

print("\n")

a.reverse()
print("Reversed array elements are:")
for i in range(0,len(a)):
    print(a[i], end=' ')


print("\n")
a.insert(2, 10)
print("Array elements after insertion are:")
for i in range(0,len(a)):
    print(a[i], end=' ')

print("\n")
a.append(11)
print("Array elements after appending are:")
for i in range(0,len(a)):
    print(a[i], end=' ')

print("\n")
a.remove(3)
print("Array elements after removing are:")
for i in range(0,len(a)):
    print(a[i], end=' ')

print("\n")
copyarray = array(a.typecode, (x*2 for x in a))
print("Copied array elements are:")
for i in range(0,len(copyarray)):
    print(copyarray[i], end=' ')