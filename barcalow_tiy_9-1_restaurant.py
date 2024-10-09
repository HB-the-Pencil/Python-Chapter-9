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

    def describe_restaurant(self):
        """
        Print some info about the restaurant.

        :return: Prints a message with the name of the restaurant and the
            type of food it serves.
        """
        print(f"{self.name} is a {self.cuisine}-style restaurant.")

    def open_restaurant(self):
        """
        "Open" the restaurant for business.

        :return: Prints a message saying that the restaurant is now open.
        """
        print(f"{self.name} is now open for business!")


# Create a new restaurant instance.
restaurant = Restaurant("Las Lomas", "Mexican")

print(restaurant.name)
print(restaurant.cuisine)

# Call methods on `restaurant`.
restaurant.describe_restaurant()
restaurant.open_restaurant()