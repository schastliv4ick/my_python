a = int(input())
sign = "+" if a >=0 else "-"
a = sign + f"{abs(a):09d}"

b = float(input())
b = f"{b:.2f}"
b = '#'*(10 - len(b)) + b

c = f"{int(input()):016b}"
l_c = [c[i:i+4]for i in range(0, 16, 4)]

print(a)
print(b)
print('_'.join(l_c))