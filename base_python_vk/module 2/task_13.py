def formating(str):
    if str[0] == '!':
        return str[1:].upper()
    str = str.replace("!", '').replace("@", '').replace("#", '').replace("%", '')
    return str.lower()

str = input()
while str != "":
    print(formating(str))
    str = input()