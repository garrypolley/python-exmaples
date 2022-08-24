import abc

"""
Purpose of this module is to show a way to implement a repository pattern where the consumer
does not care what repository is used. There will be an outside piece of data that indicates which repo to use.

In this case the caller wants to get Fruit but doesn't care if it's from a gas station or the grocery store.
In the scenario of our get Fruit -- we'll let that outside data be "worker_preference"
"""
class GetFruitRepository(abc.ABC):
    """
    Base class that ensures the implement a get_item method
    """

    @abc.abstractmethod
    def get_fruit_by_name(name: str):
        raise NotImplementedError("Did not implement get_fruit_by_name")


class GetFruitFromGasStation(GetFruitRepository):

    def get_fruit_by_name(self, name):
        return f"Gas Station: {name}"


class GetFruitFromGroceryStore(GetFruitRepository):

    def get_fruit_by_name(self, name):
        return f"Grocery Store: {name}"


class FruitFactory:
    """
    By changing the `worker_preference` on this class the underlying way to get a fruit changes

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """

    worker_preference = "gas_station"

    @staticmethod
    def repo() -> GetFruitRepository:
        if FruitFactory.worker_preference == 'gas_station':
            return GetFruitFromGasStation()
        elif FruitFactory.worker_preference == 'grocery':
            return GetFruitFromGroceryStore()
        raise ValueError(f"Not a valid worker_preference of {FruitFactory.worker_preference}")


class Bananas(FruitFactory):
    """
    A Banana class that gets from an "I don't care" FruitFactory

    Example usage:
    >>> bananas_instance = Bananas()
    >>> bananas_instance.get_all()
    'Gas Station: Banana'
    >>> FruitFactory.worker_preference = 'grocery'
    >>> bananas_instance.get_all()
    'Grocery Store: Banana'
    >>> FruitFactory.worker_preference = 'gas_station'
    >>> bananas_instance.get_all()
    'Gas Station: Banana'
    >>> FruitFactory.worker_preference = 'cause_an_error'
    >>> bananas_instance.get_all()
    Traceback (most recent call last):
    ...
    ValueError: Not a valid worker_preference of cause_an_error
    """

    def get_all(self):
        return self.repo().get_fruit_by_name("Banana")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
