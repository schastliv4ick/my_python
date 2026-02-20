str = input()
flag = False
if ('a' in str or 'o' in str) and not('i' in str or 'e' in str):
    for _ in str:
        if _ in "qwertyuiopasdfghjklzxcvbnm":
            flag = True
            
print(flag)