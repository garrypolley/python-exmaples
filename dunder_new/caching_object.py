global_thing = {}



class RecursiveNew:
    """
    Testing out having a new method that only produces one call to super new.
    This can be useful if a class is largely stateless and there is a large amount
    of computation that needs to occur when the class is initially created.

    >>> ex1 = RecursiveNew(1)
    Calling New
    Creating new class with lots of work in super
    The self.thing=1
    >>> ex2 = RecursiveNew(2)
    Calling New
    The self.thing=2
    >>> ex3 = RecursiveNew(3)
    Calling New
    The self.thing=3
    """
    def __init__(self, thing):
        self.thing = thing

        print(f"The {self.thing=}")

    def __new__(cls, thing = None):
        print("Calling New")
        new_class = global_thing.get("new_thing", None)
        if "new_thing" not in global_thing:
            print("Creating new class with lots of work in super")
            new_class = super(RecursiveNew, cls).__new__(cls)
            global_thing["new_thing"] = new_class
        return new_class

if __name__ == "__main__":
    import doctest
    doctest.testmod()
