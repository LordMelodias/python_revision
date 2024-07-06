tuple1 = ("Rohit", "Chawhan", "Python", "Django", 63.67)
print(tuple1)
print(type(tuple1))

# count check how many time the elements is repeated
a = tuple1.count("Rohit")
print(a)

# Slicing
print("Slicing Tuple: ",tuple1[0:2])
print(tuple1[0:])
print(tuple1[:4])
print(tuple1[:-3])

# Repetition
tup4 = ("Python", "Revision")
print(tup4*3)


# index check elements position in list in my chase rohit is o index position
b = tuple1.index("Rohit")
print(b)

# Nested Tuple:
nes_tup = ("Python", {4,5,6,8,7}, (2,5,8,6))
print("A nested Tuple: ", nes_tup)

# We can create tuple by using without parenthesis
tuple8 = 4,5.5,"Rohit","Chawhan"
print(tuple8)
print(type(tuple8))