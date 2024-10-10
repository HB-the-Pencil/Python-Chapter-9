from random import choice

lottery_drawings = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "1", "2", "3", "4", "5",
]

winning_ticket = ""
for i in range(4):
    chosen = choice(lottery_drawings)

    # Ensure there are no duplicates.
    lottery_drawings.remove(chosen)
    winning_ticket += chosen

# Print the winning ticket.
print("Any ticket matching the following wins:")
print(winning_ticket)