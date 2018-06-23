line1 = set(input(" Enter the string : "))

line2 = set(input(" Enter the string : "))

s = line1.union(line2)
print(s)

line1 = set(input(" Enter the string"))
line2 = set(input(" Enter the string"))
s = line1.intersection(line2)
print(s)

line1 = set(input(" Enter the string"))
line2 = set(input(" Enter the string"))
s = line1.isdisjoint(line2)
print(s)