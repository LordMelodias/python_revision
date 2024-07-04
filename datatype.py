#  What is Data Type?
# Data types is an attribute associated with a piece of data that tells a computer system how to interpret its value.

# Different types of data ?
"""
1.	Numeric
2.	Dictionary
3.	Boolean
4.	Set
5.	Sequence type
"""
# -----------------------------------------------------
# Numeric
# 1) Int, 2) Float, 3) Complex

# Code:
a = 5
print("the type of a ", type(a))

b = 5.2
print("the type of b ", type(b))

c = 1+3j
print("The type of c ", type(c))

# -----------------------------------------------------

#  Sequence Type
# 1) String, 2) List, 3) Tuple

# code:
# 1) String
str1 = "Hello"
str2 = "Rohit Chawhan"
print(str1)

#  str1 Letter 0=H  1=e  2=l  3=l  4=o
print("Print 4 letter in str1 ", str1[3])  
print("Print 1st to 3rd letter", str1[0:3])
print("Print Hello 3 time: ", str1*3)
print("Print str1 and str2 together: ", str1 +" "+str2)

# 2) List: elements are Ordered, indexed, Mutable(can be changed), Duplicate allowed, 
list1 = [1, "hi", "rohit", 2]
print(list1)
print(list1[1])
list2 = [3, "hello", "Chawhan", 4]
print(list1 + list2)
print(list1 * 2)

# 3) Tuple: elements are Ordered, indexed, Immutable, Duplicate allowed, 
tuple1 = ("hi", "Rohit", "Chawhan")
print(tuple1)
print(tuple1[1])
tuple2 = (3, "hello", "Chawhan", 4)
print(tuple1 + tuple2)
print(tuple1 * 2)

# Boolean
bo = True
print(bo)
print(type(bo))

# Set
#  Elements are unordered, not indexed, mutable(only adding and removing), Duplicated Not allowed.
set1 = {"Rohit", "Chawhan", 10, 80}
print(set1)
print(type(set1))
# Add element in set
set1.add("DragonBallZ")
print(set1)
#  Remove element from set
set1.remove(80)
print(set1)


# Dictionary
# elemets are ordered, key, mutable, duplicate allowed, key can be changed
dict1 = {1: 'Rohit', 2: 'Chawhan', 3: 'Python'}
print(dict1)
print(type(dict1))
print(dict1.keys())
