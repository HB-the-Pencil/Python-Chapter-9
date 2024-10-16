"""
Two classes to represent different types of candies.

Also includes a function to create one of these objects based on input.
"""

class Candy:
    """A basic candy. Includes name, cost, and if the candy is chocolate."""

    def __init__(self, name: str, cost: float, chocolate: bool):
        """
        Initialize the candy's name and cost.

        :param name: Name of the candy (WITHOUT punctuation).
        :param cost: Cost of the candy.
        :param chocolate: Whether the candy can be considered chocolate.
        """
        self.name = name
        self.cost = cost
        self.chocolate = chocolate

    def __repr__(self):
        """
        Represent the candy in such a way that it can be recreated.

        :return: Returns the call needed to create an identical object.
        """
        represent = (f"Candy({repr(self.name)}, {repr(self.cost)}, "
                     f"{repr(self.chocolate)})")
        return represent


class Gummy(Candy):
    """A specific type of candy: a gummy candy."""

    def __init__(self, name: str, cost: float, sour: bool):
        """
        Initialize the gummy candy with its name and cost.

        :param name: Name of the candy (WITHOUT punctuation).
        :param cost: Cost of the candy.
        :param sour: Whether the candy is sour.
        """
        # Since gummies are not chocolate, we can default chocolate to False.
        super().__init__(name, cost, False)
        self.sour = sour

    def __repr__(self):
        """
        Represent the candy in a such a way that it can be recreated.

        :return: Returns the call needed to create an identical object.
        """
        represent = (f"Gummy({repr(self.name)}, {repr(self.cost)}, "
                     f"{repr(self.sour)})")
        return represent


def create_candy():
    """
    Create a candy from user input.

    :return: Returns a new Candy object or Gummy object.
    """
    name = input("Enter the name of the candy (without punctuation).\n"
                 "Type QUIT to quit. > ")
    name = name.strip().lower()
    if name == "quit":
        print()
        return None

    cost = input("\nEnter the price of the candy (no dollar sign).\n"
                  "Type QUIT to quit. > ")
    if cost.lower().strip() == "quit":
        print()
        return None
    else:
        cost = float(cost)

    gummy = input("\nIs the candy gummy? (y/n)\n"
                  "Type QUIT to quit. > ")

    if gummy == "y":
        gummy = True
    elif gummy == "quit":
        print()
        return None
    else:
        gummy = False

    if gummy:
        sour = input("\nIs the candy sour? (y/n)\n"
                     "Type QUIT to quit. > ")
        if sour == "y":
            sour = True
        elif sour == "quit":
            print()
            return None
        else:
            sour = False

        print()
        return Gummy(name, cost, sour)

    else:
        chocolate = input("\nIs the candy chocolate? (y/n)\n"
                          "Type QUIT to quit. > ")
        if chocolate == "y":
            chocolate = True
        elif chocolate == "quit":
            print()
            return None
        else:
            chocolate = False

        print()
        return Candy(name, cost, chocolate)


# This code was used to create a list, but is no longer needed.
# quitting = False
#
# candy_list = []
#
# while not quitting:
#     candy = create_candy()
#     if not candy:
#         quitting = True
#     else:
#         candy_list.append(candy)
#
# print(candy_list)