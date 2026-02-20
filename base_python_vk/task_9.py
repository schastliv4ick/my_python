s = input().lower()

a = []
for i in s:
    if i != ' ' and i not in a:
        a.append(i)
a.sort()
print(' '.join(map(str, a)))


print(' '.join(sorted(set(input().replace(' ', '').lower()))))