
def validate_value(v):
    """
    Helper function to validate the given input is a "valid id" which is an
    int or a string.
    """
    if isinstance(v, int):
        assert v >= 0
    elif isinstance(v, str) and v.isdigit():
        assert int(v) >= 0
    else:
        assert v is not "" and v is not None
    return v

# Depending on how this file is ran this will raise an exception or not.
# python assert_example.py
# above raises the error
# below does not
# python -O assert_example.py
assert validate_value(1) == 1
assert validate_value({})
