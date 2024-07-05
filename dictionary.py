dict1 = {1: 'Rohit', 2: 'Chawhan', 3: 'Python', 'Framework': 'Django', 'birth': 2004}

print(dict1)
print(type(dict1))
# %s mean string
print("Developer: %s" %dict1[1])
# %d mean integers
print("Birth Year: %d" %dict1['birth'])
print("Python: %s" %dict1['Framework'])

del dict1[2]
print("After delete element 2")
print(dict1)

# sorted(dict1) is only support when the key are numerical

# with for loop
for x in dict1:
    print(dict1[x])
    
# wiht for loop items
for y in dict1.items():
    print(y)

dict1.clear()
print(dict1)

# with input
Employee = {"Name": "Rohit", "Age": 20, "salary":80000,"Company":"Microsoft"}         
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)        
print("Enter the details of the new employee..");        
Employee["Name"] = input("Name: ");        
Employee["Age"] = int(input("Age: "));        
Employee["salary"] = int(input("Salary: "));        
Employee["Company"] = input("Company:");        
print("printing the new data");        
print(Employee)  

