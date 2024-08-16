val = int(input("Enter a number: "))
print("Entered number is ", val)
n1 = 0
n2 = 1
count = 0

if(val<=0):
    print("Please enter a positive number")
elif(val==n1):
    print("Sequence: ",n1)
else:
    while(count<val):
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count+=1
