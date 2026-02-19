n = int(input())
res = []

for i in range(n):
    l = list(map(int, input().split()))
    res.append(max(l))


res.sort(reverse=True)
print(';'.join(map(str,res)))
