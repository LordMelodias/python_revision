val = int(input("Enter a number: "))
print("Entered number is ", val)
fact =1

for i in range(1,val+1):
    fact= fact * i
    
print(fact, "!")
