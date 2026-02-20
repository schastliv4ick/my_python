s = input()
s = s.replace("!", "").replace(",", "").replace(".", "").replace("?", "").replace(";", "").replace(":", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace(",", "")
s = s.lower().split(' ')

res = []
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
    if len(i) >= 5 and len(set(i)) >= 4 and d[i] > 2:
        res.append(i)

print('\n'.join(sorted(set(res))))