from random import randint

class Die:
    """Class representing a die with certain number of sides."""

    def __init__(self, sides: int):
        """
        Initialize a die with a certain number of sides.

        :param sides: Number of sides on the die.
        """
        self.sides = sides

    def roll_die(self):
        """
        Rolls the die and returns the result.

        :return: Prints the result of the roll.
        """
        roll = randint(1, self.sides)
        print(roll)


# Create and roll a 10-sided die.
d10 = Die(10)
print("d10 rolls:")
for i in range(10):
    print(i+1, end=". ")
    d10.roll_die()

# Create and roll a 20-sided die.
d20 = Die(20)
print("\nd20 rolls:")
for i in range(10):
    print(i+1, end=". ")
    d20.roll_die()