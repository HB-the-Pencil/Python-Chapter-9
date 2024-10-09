class User:
    """Models a user (of a website, etc)."""

    def __init__(self, first_name: str, last_name: str, age: int,
                 location: str, pronouns: list = None):
        """
        Initialize a user with a first and last name, age, location, and
        pronouns.

        :param first_name: User's first name.
        :param last_name: User's last name.
        :param age: User's age.
        :param location: User's location.
        :param pronouns: List of user's pronouns (subject, object, possessive
            adjective, possessive pronoun). They/them/their/theirs by default.
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location
        if not pronouns:
            pronouns = ["they", "them", "their", "theirs"]
        self.pronouns = pronouns
        self.verb = "are" if "they" in self.pronouns else "is"

    def describe_user(self):
        """
        Describe the user.

        :return: Print a string with the user's attributes.
        """
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"{self.pronouns[0].title()} {self.verb} living in "
              f"{self.location}.")

    def greet_user(self):
        """
        Print a greeting for a user.

        :return: Print a string greeting the user by name.
        """
        print(f"Welcome, {self.first_name} {self.last_name}!")


# Create some users.
parzival = User("Wade", "Watts", 18, "Columbus, Ohio",
                ["he", "him", "his", "his"])
art3mis = User("Samantha", "Cook", 19, "Columbus, Ohio",
               ["she", "her", "her", "hers"])
void = User("void", "walker", 34, "Reykjavik")

# Two guesses as to what I was listening to while I coded...
lonely_person = User("Eleanor", "Rigby", 58, "London",
                     ["she", "her", "her", "hers"])

# Create a list of users, which makes it easier to manipulate.
users = [parzival, art3mis, void, lonely_person]
for user in users:
    user.describe_user()
    user.greet_user()
    print()