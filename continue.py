# continue use in range 1 to 10
#  continue: A continue statement is used to force the loop to skip the remaining code and start the next iteration.
for i in range(1,10):
    if i==5:
        continue
    print(i)
    
# pass: A pass statement signals to a loop that there is “no code to execute here.” It's a placeholder for future code
for j in range(5):
    if j % 2 == 0:
        pass  # Placeholder for even number handling
    else:
        print(i)


print("-------------------------------------------")

for j in range(2,100):
    if j%2==0:
        if j==56:
            continue
        print(j)
        