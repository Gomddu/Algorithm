a,b=map(int,input().split())
num = list(map(int, input().split()))
arr=[]
for i in range(a):
    if num[i] < b:
        arr.append(num[i])
for i in range(len(arr)):
    print(arr[i],end=" ")