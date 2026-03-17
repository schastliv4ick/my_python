import functools

def circuit_breake(func, state_count, error_count, network_errors, sleep_time_sec):
    @functools.wraps
    def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
    

def decorator(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for I in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator