# Decorators

Here are some examples of using decorators in Python.

The first one here is all about how you can have a "Cache".

Note, these only use class based decorators, because I find these easier to reason about.

## Usage

Here is what it looks like to test out and see the `cache_data.py`:

```
(decorators) ➜  decorators git:(main) python cache_data.py -v
Trying:
    @cache_data
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
Expecting nothing
ok
Trying:
    fibonacci.cache
Expecting:
    {}
ok
Trying:
    fibonacci(3)
Expecting:
    2
ok
Trying:
    fibonacci.cache
Expecting:
    {(1,): 1, (0,): 0, (2,): 1, (3,): 2}
ok
Trying:
    @cache_data
    def sum(a, b):
        return a + b
Expecting nothing
ok
Trying:
    sum.cache
Expecting:
    {}
ok
Trying:
    sum(1, 2)
Expecting:
    3
ok
Trying:
    sum.cache
Expecting:
    {(1, 2): 3}
ok
Trying:
    sum(5, 6)
Expecting:
    11
ok
Trying:
    sum.cache
Expecting:
    {(1, 2): 3, (5, 6): 11}
ok
3 items had no tests:
    __main__
    __main__.cache_data.__call__
    __main__.cache_data.__init__
1 items passed all tests:
  10 tests in __main__.cache_data
10 tests in 4 items.
10 passed and 0 failed.
Test passed.
```
