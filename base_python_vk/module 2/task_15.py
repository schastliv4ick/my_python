n = int(input())
if n > 30 or n < 1:
    print("error")

flist = [1, 1]

def fib(flist, n):
    if len(flist) >= n:
        return flist
    flist.append(flist[-1]+flist[-2])
    fib(flist, n)

fib(flist, n)
print(flist[n-1])
    