num = int(input("Enter a number: "))
result = 0
temp = num
while(num>0):
    a = num%10
    result+=a*a*a
    num = num//10
    
if temp==result:
    print(result, " is a Armstrong Number")
else:
    print(result, " is not a Armstrong Number")
