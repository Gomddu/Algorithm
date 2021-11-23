a = int(input())
num = list(map(int, input().split()))
k = max(num)
for i in range(a):
    num[i] = num[i]/k * 100
result = sum(num) / a
print(result)