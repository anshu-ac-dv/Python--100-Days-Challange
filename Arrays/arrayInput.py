from array import*

a = array('i',[])
n = int(input("Enter the Size of array:"))

# Taking input from the user and adding it to the array
for i in range(0,n):
    a.append(int(input("Enter the element:")))

# Printing the elements of the array
print("The elements in the array are:")
for i in range(0,n):
    print(a[i])

