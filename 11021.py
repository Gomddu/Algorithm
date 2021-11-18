a = int(input())
arr=[]
for i in range(a):
    b,c=map(int,input().split())
    arr.append(b+c)
for j in range(a):
    print("Case #" + str(j+1) + ": " + str(arr[j]))