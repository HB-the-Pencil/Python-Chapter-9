from random import choice

my_ticket = "ad3i"
winning_ticket = ""

attempts = 0

def generate_ticket():
    """
    Function to generate a lottery ticket.

    :return: Returns a sequence of four random letters and numbers.
    """
    ticket = ""
    lottery_drawings = [
        "a", "b", "c", "d", "e",
        "f", "g", "h", "i", "j",
        "1", "2", "3", "4", "5",
    ]

    for i in range(4):
        chosen = choice(lottery_drawings)

        # Ensure there are no duplicates.
        lottery_drawings.remove(chosen)
        ticket += chosen

    return ticket

def nice_number(num: float, is_float = False):
    """
    Return a nicely formatted version of a number.

    :param num: Number to format.
    :param is_float: Whether to return values after the decimal point.

    :return: A number, separated by commas.
    """
    # Turn the number into a string so it can be iterated over.
    num = str(float(num)).split(".")
    returning = ""

    # Work backwards to add commas.
    for i in range(-len(num[0]), 0):
        if i != -len(num[0]) and i % 3 == 0:
            returning += ","
        returning += num[0][i]

    # If the user wants the bit after the decimal point, add it.
    if is_float:
        returning += "." + num[1]

    return returning

# While I am not winning, repeat the choice process.
while my_ticket != winning_ticket:
    winning_ticket = generate_ticket()
    attempts += 1

# Print the winning ticket.
print(f"It took {nice_number(attempts)} attempts to win the lottery.")
