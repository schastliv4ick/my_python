def map(func, seq):
    return [str(func(x)) for x in seq]

func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
   print(x)
