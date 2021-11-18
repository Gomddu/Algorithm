import sys
input = sys.stdin.readline
arr=[]
a = int(input())
for _ in range(a):
    b,c = map(int, input().split())
    arr.append(b + c)
for  i in range(a):
    print(arr[i])
