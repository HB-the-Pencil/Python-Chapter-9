from barcalow_chapter_9_candy_list import Candy, Gummy

candies = [
    Candy('hershey bar', 1.39, True),
    Candy('reeses cup', 1.39, True),
    Candy('almond joy', 1.99, True),
    Candy('skittles', 1.29, False),
    Gummy('haribo goldbears', 0.9, False),
    Gummy('sour patch kids', 1.99, True),
    Candy('life savers', 1.98, False),
]

candy_dict = {}

for candy in candies:
    candy_dict[candy.name] = candy

# Print a welcome message.
welcome = """+===================+
|  Welcome to the   |
|  PyCandy Store!   |
|~~~~~~~~~~~~~~~~~~~|
|  Press Enter to   |
|  see our current  |
|  inventory.       |
+===================+
"""
input(welcome)

# Print out the dictionary of candies. (Really, it would work to just use the
# list and access different properties...)
for name, candy in candy_dict.items():
    print(f"+ {name.title()} ...... ${candy.cost:.2f}")

# Enter the order system.
print("\n=== Ordering Candy ===")
order = []

while True:
    command = input("Please choose a candy to add to your order.\n"
                    "Type QUIT to quit. > ")
    # Clean the command.
    command = command.strip().lower()

    # Quit the loop if the user asks to quit.
    if command == "quit":
        break

    # Make sure there's input to work with.
    if command == "":
        print("Enter a candy's name!")
        continue

    # Add unknown candies to the dictionary.
    if command not in candy_dict:
        print(f"\nThe candy \"{command}\" isn't in our registry. "
              f"Let's add it.")

        # The name has already been provided.
        name = command

        # Get the cost, or quit.
        cost = input("\tHow much does the candy cost?\n\t"
                     "Type CANCEL to cancel adding the candy. > ")

        if cost.lower().strip() == "cancel":
            print("\tReturning to order selection...\n")
            continue

        # My friend helped find this pretty important bug!
        try:
            cost = float(cost)
        except ValueError:
            cost = input("\tMake sure the price is a number. > ")
            try:
                cost = float(cost)
            except ValueError:
                cost = input("\tOne more try. > ")
                try:
                    cost = float(cost)
                except ValueError:
                    print("\tPrice was not a number. Returning to order "
                          "selection...\n")
                    continue

        # Get the gummy property.
        gummy = input("\n\tIs the candy a gummy candy? (y/n)\n\t"
                     "Type CANCEL to cancel adding the candy. > ")

        gummy = gummy.lower().strip()

        if gummy == "cancel":
            print("\tReturning to order selection...\n")
            continue
        elif gummy == "y":
            gummy = True
        else:
            gummy = False

        # If the candy is gummy, check if it's sour too.
        if gummy:
            sour = input("\n\tIs the candy sour? (y/n)\n\t"
                         "Type CANCEL to cancel adding the candy. > ")
            sour = sour.lower().strip()

            if sour == "cancel":
                print("\tReturning to order selection...\n")
                continue
            elif sour == "y":
                sour = True
            else:
                sour = False

            print()
            candy_dict[name] = Gummy(name, cost, sour)

        # Otherwise, check if it's chocolate.
        else:
            chocolate = input("\n\tIs the candy chocolate? (y/n)\n\t"
                              "Type CANCEL to cancel adding the candy. > ")
            chocolate = chocolate.strip().lower()

            if chocolate == "cancel":
                print("\tReturning to order selection...\n")
                continue
            elif chocolate == "y":
                chocolate = True
            else:
                chocolate = False

            print()
            candy_dict[name] = Candy(name, cost, chocolate)

    # At last, add the candy to the user's order.
    print(f"\tAdding {command.title()} to your order...\n")
    order.append(candy_dict[command])

# Print the user's receipt.
print("\n=== Your Order ===")
subtotal = 0
for candy in order:
    print(f"+ {candy.name.title()} ...... ${candy.cost:.2f}")
    subtotal += candy.cost

# Subtotal, tax, and total.
print("+ ================================")
print(f"+ Subtotal ...... ${subtotal:.2f}")
print(f"+ Tax (7%) ...... ${(0.07*subtotal):.2f}")
print(f"+ Total ....... ${(1.07*subtotal):.2f}")

# Print a goodbye message.
print("\n\tThank you! Have a nice day!")