from array import*

a = array('i', [1, 2, 3, 4, 5])
a.reverse()
print("Reversed array elements are:")
for i in range(0,len(a)):
    print(a[i], end=' ')