import weakref

default_color = "brown"

class ColorContextMixin:
    """
    Used to manage the color of the thing.
    """
    _context_color = None
    _instances = []

    def __init__(self, color=default_color) -> None:
        self.__class__._instances.append(weakref.proxy(self))

        # Track the original color so it works inside and outside
        # the context manager whenever the class is instantiated.
        self._original_color = color

        if self.context_color is not None:
            self.color = self.context_color
        else:
            self.color = color

    @property
    def context_color(self):
        return self._context_color

    @context_color.setter
    def context_color(self, color):
        self._context_color = color
        self.color = color



class Bear(ColorContextMixin):

    def log_bear(self):
        print(f"The bear is {self.color}")


class Dog(ColorContextMixin):

    def log_dog(self):
        print(f"The dog is {self.color}")


class ColorContext:
    """
    Should be used with the `ColorContextMixin` to allow to set the color for all classes
    that care about sharing color when used in a context.

    Example usage:

    >>> color_context = ColorContext
    >>> my_bear = Bear()
    >>> my_bear.log_bear()
    The bear is brown
    >>> my_dog = Dog()
    >>> my_dog.log_dog()
    The dog is brown
    >>> with color_context(color="red"):
    ...     my_dog.log_dog()
    ...     my_bear.log_bear()
    The dog is red
    The bear is red
    >>> my_dog.log_dog()
    The dog is brown
    >>> my_bear.log_bear()
    The bear is brown
    >>> with color_context(color="blue"):
    ...     my_dog.log_dog()
    ...     my_bear.log_bear()
    The dog is blue
    The bear is blue
    >>> my_blue_dog = Dog(color="blue")
    >>> my_blue_dog.log_dog()
    The dog is blue
    >>> with color_context(color="red"):
    ...     my_blue_dog.log_dog()
    The dog is red
    >>> my_blue_dog.log_dog()
    The dog is blue
    >>> with color_context(color="green"):
    ...    new_bear = Bear(color="ignored_because_the_context_manager")
    ...    new_bear.log_bear()
    The bear is green
    >>> new_bear.log_bear()
    The bear is ignored_because_the_context_manager
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
            defined_class._context_color = self.color

        # define this for all classes that are already defined
        for class_instance in ColorContextMixin._instances:
            class_instance.context_color = self.color

        return self

    def __exit__(self, *ignored_args):
        """
        Upon exiting the context manager the color will be reset to the default color.
        """
        # For each subclass that was changed, unchange it
        for defined_class in ColorContextMixin.__subclasses__():
            defined_class._context_color = None


        # For each instance undo the change
        for class_instance in ColorContextMixin._instances:
            class_instance.color = class_instance._original_color
            class_instance._context_color = None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
