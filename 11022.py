a = int(input())
arr=[]
brr=[]
crr=[]
for i in range(a):
    b,c=map(int,input().split())
    arr.append(b+c)
    brr.append(b)
    crr.append(c)
for j in range(a):
    print("Case #" + str(j+1) + ": "+ str(brr[j]) + " + "+ str(crr[j]) + " = " + str(arr[j]))