a,b = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0

for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            if arr[i] + arr[j] + arr[k] > b:
                continue
            else:
                sum = max(sum, arr[i]+arr[j]+arr[k])
print(sum)