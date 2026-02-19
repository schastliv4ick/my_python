def format_float_smart(number):
    str_num = str(number)
    
    if '.' in str_num:
        integer_part, decimal_part = str_num.split('.')
        if len(decimal_part) > 2:
            return f"{number:.2f}"
        else:
            return str_num
    return str_num

s = list(len(a) for a in input().split())
print(format_float_smart(sum(s) / len(s)))

