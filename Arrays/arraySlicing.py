from array import*

a = array('i',[1,2,3,4,5])

b = a[1:4] # Slicing the array from index 1 to 3
c = a[2:5] # Slicing the array from index 2 to 4
print("Sliced array:", b)
print("Sliced array:", c)

d = a[::-1] # Slicing the array in reverse order
print("Reversed array:", d)