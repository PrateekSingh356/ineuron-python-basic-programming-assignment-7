#2. Write a Python Program to find largest element in an array?
arr=[1,2,3,4,5,6,7,8,9,10]
def find(x):
    for i in range(len(arr)):
        if int(arr[i]) == x:
            return i

x = int(input("enter the numberto be find: "))
print(f'element found at : {find(x)+1}')
