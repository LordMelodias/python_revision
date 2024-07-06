# What is lambda?
# We used lambda the lambda keyword in Python to define an unnamed function.
# Example:
add = lambda num: num + 4
print(add(6))

'''
How above lamda look:
Syntax: lambda arguments: expression   

def add( num ):  
   return num + 4  
print( add(6) ) 
'''
# Example: Write a program for table
num = int(input("Enter a number: "))
for i in range(1,11):
    table = lambda x: num*x
    print(table(i))
 
