#3. Write a Python Program for array rotation?
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
i1 = len(arr)
for i in range(i1):
    temp = arr[i]
    arr[i] = arr[i1-1]
    arr[i1-1] = temp
    i1-=1
    if i==5:
        break
print(arr)