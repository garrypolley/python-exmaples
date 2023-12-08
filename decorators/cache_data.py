"""
Helper function for caching data via a decorator.

It'll add the "cache" to the function object itself, so that it can be accessed
later.
"""

class cache_data(object):
    """
    Helper function to cache return values from a call. This is largely an example of
    showing how the decorator can _mutate_ the function object itself.

    Example:
    >>> @cache_data
    ... def fibonacci(n):
    ...     if n < 2:
    ...         return n
    ...     else:
    ...         return fibonacci(n-1) + fibonacci(n-2)
    >>> fibonacci.cache
    {}
    >>> fibonacci(3)
    2
    >>> fibonacci.cache
    {(1,): 1, (0,): 0, (2,): 1, (3,): 2}
    >>> @cache_data
    ... def sum(a, b):
    ...     return a + b
    >>> sum.cache
    {}
    >>> sum(1, 2)
    3
    >>> sum.cache
    {(1, 2): 3}
    >>> sum(5, 6)
    11
    >>> sum.cache
    {(1, 2): 3, (5, 6): 11}
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value


@cache_data
def fibonacci(n):
    """
    Example Usage:
    >>> fibonacci(2)
    1
    >>> fibonacci.cache
    {(1,): 1, (0,): 0, (2,): 1}
    """
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@cache_data
def sum(a, b):
    """
    Example Usage:
    >>> sum(1, 2)
    3
    >>> sum(5, 6)
    11
    >>> sum.cache
    {(1, 2): 3, (5, 6): 11}
    """
    return a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
