i = 0
while 1:
    print(i, ' ', end='/')
    i+=1
    if i==5:
        break
print("When 5 came it break loop")

str1 = 'Python'
for char in str1:
    if char=='o':
        break
    print(char)
    

n = 2
while True:
    i = 1
    while i<=10:
        print("%d X %d = %d\n" % (n,i,n*i))
        i+=1
    choice = int(input("Do you want to continue printing table press 0 for no: "))
    if choice==0:
        print("Exiting Program")
        break
    n+=1
print("Program finished Successfully")