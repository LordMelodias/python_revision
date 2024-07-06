list1 = ['Hello', 'Rohit', 'Chawhan', 'Django']
print(list1)
print(list1[1])

# append will add value from back
list1.append('Flask')
print(list1)

# insert will add value by index position
list1.insert(3, 'Python')
print(list1)

# pop will remove elements from back 
list1.pop()
print(list1)

# reverse use to reverse elements of list
list1.reverse()
print(list1)

# Copy used to copy the whole list with elements
list2 = list1.copy()
print(list2)

# clear will remove all elements from list
list1.clear()
print(list1)

emp=["Rohit", 666, "India"]
Dep1 = ["CS", 12]
Dep2 = ["IT", 54]
Hod_CS = [50, "Mr_Surya"]
Hod_IT = [70, "Mr_Riya"]
print("Employee Name: %s, ID: %d, Country: %s" %(emp[0], emp[1], emp[2]))
print("Department 1:")
print("Name: %s, ID: %d" %(Dep1[0], Dep1[1]))
print("Department 2:")
print("Name: %s, ID: %d" %(Dep2[0], Dep2[1]))
print("Computer Science Department: ")
print("Name: %s, ID: %d" %(Hod_CS[1], Hod_CS[0]))
print("Information Technology Department: ")
print("Name: %s, ID: %d" %(Hod_IT[1], Hod_IT[0]))