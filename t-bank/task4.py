n, m = map(int, input().split())
g = [n][n]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = 1
way = []
res_ways = []

res_ways

def cicl(s, n, g, way):
    for i, j in (range[s, n], g[i]):
        way.append(i)
        if j == 1 and way[0] == i:
            return way
        elif j == 1 and way[-1] != i:
            cicl()