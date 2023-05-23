## Assert

Some examples about using assert.

This specifically is to show that assert does not always do what we think it does. And should
likely only be used in tests.

### Raises an error

If you run Python without any modification you'll see the following:

```sh
➜  assert git:(main) python assert_example.py
assert_example.py:12: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  assert v is not "" and v is not None
Traceback (most recent call last):
  File "assert_example.py", line 16, in <module>
    assert validate_value({})
AssertionError
```

If you run in an optimized mode you'll see the following:

```sh
➜  assert git:(main) ✗ python -O assert_example.py
```


Which is to say, no error happens and the code "passes" even though it "should" fail.

We should not assume the runtime of our code, and thus only use asserts in tests, not in "production" code, unless test rely on the asserts to cause failure. (though that may not be great either, different topic entirely.)
