def filter(func, seq):
   return [x for x in seq if func(x)]

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)