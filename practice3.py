#44. Write a Python Program to Split the array and add the first part to the end?
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
arr1=[]
x = len(arr)
for i in range(round(x/2)):
    arr1.append(arr[i])
for i in range(round(x/2)):
    arr.remove(arr1[i])
for i in range(len(arr1)):
    arr.append(arr1[i])
print(arr)