from bisect import bisect_right, bisect_left
_ = int(input())
cards = sorted(map(int, input().split()))
_ = int(input())
qry = list(map(int, input().split()))
ans = []
for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    ans.append(1 if r - l else 0)
print(*ans)