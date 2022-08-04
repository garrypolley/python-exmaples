# Context Managers

This folder contains examples of using context managers and trying them out.

As a consumer a context manager looks like:

```python

with some_thing:
    something.in_context()
```


## Looking at examples

The files have far more detail on usage and what they expect. The doc tests should show what is expected as well.

* color_context_manager: `python color_context_manager.py -v` -- context manager that manages colors between classes (Dog and Bear)
* forced_context_manager: `python forced_context_manager.py -v` -- context manager that forces usage with using the colors
