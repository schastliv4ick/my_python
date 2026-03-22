#s = input()
s="68002034"
cnt = 0
s = ''.join(sorted(list(s)))
while s[0] == '0':
    s = s[1:]
    cnt += 1
s = s[0] + '0'*cnt + s[1:]
print(s)