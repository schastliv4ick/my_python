n = int(input())
m = int(input())
f = True
a = input()
while (a  != ''):
    if int(a) < n or int(a) > m:
        f = False
    a = input()
print(f)