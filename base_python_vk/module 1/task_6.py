str = input()

str = str.lower()
str_new = str.replace("!", '').replace("%", '').replace("#", '').replace("@", '')
print(len(str) - len(str_new))
print(str_new)