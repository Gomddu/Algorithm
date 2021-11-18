a= int(input())
arr = []
for _ in range(a):
    b, c = map(int, input().split())
    arr.append((b+c))
for i in range(len(arr)):
    print(arr[i])