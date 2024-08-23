class Address:
    """
    A class to represent an address.

    Attributes:
        street (str): The street address.
        city (str): The city of the address.
    """

    def __init__(self, street: str, city: str):
        self.street = street
        self.city = city

    def __repr__(self) -> str:
        return f"Address(street={self.street}, city={self.city})"


class Person:
    """
    A class to represent a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        address (Address): The address of the person.

    Methods:
        __init__(name, age, address):
            Initializes the Person with a name, age, and address.
        greet():
            Returns a greeting message.
        have_birthday():
            Increases the age of the person by 1.
    """

    def __init__(self, name: str, age: int, address: Address):
        """
        Initializes the Person with a name, age, and address.

        Parameters:
            name (str): The name of the person.
            age (int): The age of the person.
            address (Address): The address of the person.

        Example:
            address = Address("123 Main St", "Anytown")
            person = Person("Alice", 30, address)
        """
        self.name = name
        self.age = age
        self.address = address

    def greet(self) -> str:
        """
        Returns a greeting message.

        Returns:
            str: A greeting message including the person's name.

        Example:
            >>> address = Address("123 Main St", "Anytown")
            >>> person = Person("Bob", 25, address)
            >>> person.greet()
            'Hello, my name is Bob.'
        """
        return f"Hello, my name is {self.name}."

    def have_birthday(self):
        """
        Increases the age of the person by 1.

        Example:
            >>> address = Address("123 Main St", "Anytown")
            >>> person = Person("Charlie", 40, address)
            >>> person.have_birthday()
            >>> person.age
            41
        """
        self.age += 1
