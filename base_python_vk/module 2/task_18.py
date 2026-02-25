def cache_deco(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code) 