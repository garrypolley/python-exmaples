import weakref
"""
Use weakref to keep track of all instances of the color context mixin. This allows
the context manager to properly modify the class instances when inside the context
manager.
"""

class ColorContextMixin:
    """
    Used to manage the color of the thing.
    """
    _instances = []
    _color = None

    def __init__(self) -> None:
        self.__class__._instances.append(weakref.proxy(self))

    @property
    def color(self):
        return self._color

    @color.getter
    def color(self):
        if self._color is None:
            raise AssertionError("Class is used outside the ColorContextManager")
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Bear(ColorContextMixin):

    def log_bear(self):
        print(f"The bear is {self.color}")


class Dog(ColorContextMixin):

    def log_dog(self):
        print(f"The dog is {self.color}")


class ColorContext:
    """
    Should be used with the `ColorContextMixin` forces all uses of the subclasses to use the
    context manager when interacting with color.

    Example usage:

    >>> color_context = ColorContext
    >>> my_bear = Bear()
    >>> my_bear.log_bear()
    Traceback (most recent call last):
    ...
    AssertionError: Class is used outside the ColorContextManager
    >>> my_dog = Dog()
    >>> my_dog.log_dog()
    Traceback (most recent call last):
    ...
    AssertionError: Class is used outside the ColorContextManager
    >>> with color_context(color="red"):
    ...     my_dog.log_dog()
    ...     my_bear.log_bear()
    The dog is red
    The bear is red
    >>> my_dog.log_dog()
    Traceback (most recent call last):
    ...
    AssertionError: Class is used outside the ColorContextManager
    >>> my_bear.log_bear()
    Traceback (most recent call last):
    ...
    AssertionError: Class is used outside the ColorContextManager
    >>> with color_context(color="blue"):
    ...     my_dog.log_dog()
    ...     my_bear.log_bear()
    The dog is blue
    The bear is blue
    >>> my_blue_dog = Dog()
    >>> with color_context(color="red"):
    ...     my_blue_dog.log_dog()
    The dog is red
    >>> my_blue_dog.log_dog()
    Traceback (most recent call last):
    ...
    AssertionError: Class is used outside the ColorContextManager
    >>> with color_context(color="green"):
    ...    new_bear = Bear()
    ...    new_bear.log_bear()
    The bear is green
    >>> new_bear.log_bear()
    Traceback (most recent call last):
    ...
    AssertionError: Class is used outside the ColorContextManager
    """
    def __init__(self, color) -> None:
        self.color = color

    def __enter__(self):
        """
        When the context manager is entered it will set the color on all classes to the color given
        the context manager. See class doc for example usage
        """
        # define this for all classes not yet used
        for defined_class in ColorContextMixin.__subclasses__():
            defined_class._color = self.color

        # define this for all classes that are already defined
        for class_instance in ColorContextMixin._instances:
            class_instance.color = self.color

        return self

    def __exit__(self, *ignored_args):
        """
        Upon exiting the context manager the color will be reset to the default color.
        """
        # For each subclass that was changed, unchange it
        for defined_class in ColorContextMixin.__subclasses__():
            defined_class._color = None


        # For each instance undo the change
        for class_instance in ColorContextMixin._instances:
            class_instance.color = None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
