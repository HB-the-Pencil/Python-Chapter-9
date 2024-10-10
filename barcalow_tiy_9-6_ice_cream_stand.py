# Couldn't figure out how to import from a TIY (the hyphen was throwing it
# off), so I just copied and pasted it.

class Restaurant:
    """Create a restaurant with a name and cuisine type."""

    def __init__(self, name: str, cuisine: str):
        """
        Initialize name and cuisine type.

        :param name: Name of the restaurant.
        :param cuisine: Type of food served.
        """
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """
        Print some info about the restaurant.

        :return: Prints a message with the name of the restaurant and the
            type of food it serves.
        """
        print(f"{self.name} is a {self.cuisine}-style restaurant.")
        print(f"They have served {self.number_served} people.\n")

    def open_restaurant(self):
        """
        "Open" the restaurant for business.

        :return: Prints a message saying that the restaurant is now open.
        """
        print(f"{self.name} is now open for business!")

    def set_number_served(self, served: int):
        """
        Set the number of customers served.

        :param served: Total number of customers served by the restaurant.
        :return: Sets the number of customers served if it is greater than the
            current number of customers served.
        """
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You can't serve fewer people than you already served.\n")

    def increase_number_served(self, served: int):
        """
        Increases the number of customers served (i.e, after a day of work).

        :param served: Number of people served (used to increase total).
        :return: Increases the number of customers served if the number is
            positive.
        """
        if served >= 0:
            self.number_served += served
        else:
            print("You can't have served negative people.\n")


class IceCreamStand(Restaurant):
    """Model an ice cream stand, a specific type of restaurant."""

    def __init__(self, name: str, flavors: list):
        """
        Initialize the ice cream stand. No need for a cuisine type.

        :param name: Name of the ice cream stand.
        """
        super().__init__(name, "ice-cream-stand")
        self.flavors = flavors

    def display_flavors(self):
        """
        Display the flavors available at this stand.

        :return: Prints a list of flavors.
        """
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print("  -", flavor)


stand = IceCreamStand("Zesto's", ["vanilla", "chocolate", "twist"])
stand.display_flavors()