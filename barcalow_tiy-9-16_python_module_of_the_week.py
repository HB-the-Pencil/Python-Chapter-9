# Random is a pretty cool module!
import random as r

# Now it doesn't have to be random :O
seed = input("Enter a random seed: ")
r.seed(seed)

# Print the result.
print(f"{r.uniform(0, 100):.3f}")

# Seed 42 always displays 47.366, at least on my computer. What does it do on
# yours?

# You can even do steps!
print(f"{r.randrange(0, 1000, 50)}")

# 450 with seed 42. (Changing the first parameter to 1 makes it 451.
# Interesting look into the process behind this.)

# For the lottery, I realize now that I could have used r.sample() to get
# just one item, rather than removing items from the list. Oh, well...

# There is also a Random class so you can have multiple generators at once!