#  Check prime number from user
num = int(input("Enter number: "))
is_pr = True

if num==1:
    print(num, "is not a prime number")
else:
    for a in range(2, num):
        if num%a ==0:
            is_pr = False
            break

if is_pr:
    print(num, "is a prime number")
else:
    print(num, " is not prime number")

print("---------------------------------------------")

#  to print prime number from 1 to 100
for i in range(2,101):
    is_prime = True
    for j in range(2, i):
        if i %j ==0:
            is_prime = False
            break
    if is_prime:
        print(i)
        
print("--------------------------------------------")
# Print prime number from 1 to 100 using while loop
b =2
c =2
while b<=100:
    is_prime = True
    while c<b:
        if b%c==0:
            is_prime = False
            break
        c+=1
    if is_prime:
        print(b, end=' ')  
    b+=1
        