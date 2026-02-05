from numpy import*

a = array([1, 2, 3, 4, 5.5, 'a'])
for i in a:
    print(i, end=' ')
print("\nArray is:", a)
print("Array shape is:", a.shape)

b = arange(1, 10, 2)
print("Array with arange:", b)
print("Array shape is:", b.shape)

c = linspace(10, 40, 5)
print("Array with linspace:", c)
print("Array shape is:", c.shape)

d = logspace(1, 40, 5)
print("Array with logspace:", d)
print("Array shape is:", d.shape)

e = arange(10, 20, 3)
print("Array with arange:", e)
print("Array shape is:", e.shape)

d = zeros((3, 4))
print("Array with zeros:\n", d)
print("Array shape is:", d.shape)

e = ones((3, 4))
print("Array with ones:\n", e)
print("Array shape is:", e.shape)

f = random.rand(3, 4)
print("Array with random values:\n", f)
print("Array shape is:", f.shape)

g = full(5, 6)
print("Array with full:\n", g)
print("Array shape is:", g.shape)

twodarray = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Two dimensional array:\n", twodarray)
print("Array shape is:", twodarray.shape)

threedarray = array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print("Three dimensional array:\n", threedarray)
print("Array shape is:", threedarray.shape)