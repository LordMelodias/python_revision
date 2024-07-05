import numpy as np
arr = np.array([10,20,30,40,50])
print(arr * 100)

for ar in arr:
    print(ar)
    
arr1 = np.array([[10,20,30], [40,50,60], [70,80,90]])

print("Element at Row 0, Column 0: ", arr1[0,0])

print("Array")
print(arr1)
print(type(arr1))

for i in arr1:
    for j in i:
        print(j)