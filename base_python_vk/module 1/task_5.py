a = int(input().strip())
b = float(input().strip())
c = int(input().strip())

# Первое число: знак и ровно 9 цифр с ведущими нулями
sign = '+' if a >= 0 else '-'
first = sign + f"{abs(a):09d}"

# Второе число: два знака после запятой, общая ширина 10, заполнение '#'
s = f"{b:.2f}"                     # например, "3.14" или "-123.70"
second = '#' * (10 - len(s)) + s

# Третье число: 16-битное двоичное представление, группы по 4 бита
bin_str = f"{c:016b}"               # 16 бит с ведущими нулями
third = '_'.join(bin_str[i:i+4] for i in range(0, 16, 4))

# Вывод
print(first)
print(second)
print(third)