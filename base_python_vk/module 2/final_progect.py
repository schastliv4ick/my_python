def cache_deco(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


def solution(func_map, func_filter, data):
    new_list = map(func_map, filter(func_filter, data))
    for i, el in enumerate(new_list):
        if i%2 == 0:
            yield(el)




code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)