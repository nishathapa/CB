ab = tuple()
print(type(ab))
a = 67
b = 45
k = (b,a)
print(type(k))
for item in k:
    a = 67
b = 45
k = (b,a)
print(type(k))
for item in k:
    print (item)
