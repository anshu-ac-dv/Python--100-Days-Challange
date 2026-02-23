from array import*

a = array('i', [1, 2, 3, 4, 5])
# Inserting an element at a specific position in the array
a.insert(2, 10)
print("Array elements after insertion are:")
for i in range(0,len(a)):
    print(a[i], end=' ')

# Appending an element to the array at the end
a.append(20)
print("\nArray elements after appending are:")
for i in range(0,len(a)):
    print(a[i], end=' ')

# Overwriting an element at a specific index
a[2] = 15
print("\nArray elements after overwriting are:")
for i in range(0,len(a)):
    print(a[i], end=' ')