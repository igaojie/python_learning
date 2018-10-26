# coding=utf-8
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    '''Docstring'''
    print('Called example function')


print(example.__name__, example.__doc__)


def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2018-10-26')


now()
