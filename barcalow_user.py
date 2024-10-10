"""A class to represent a user."""

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

        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """
        Increase the number of attempted logins.

        :return: Adds 1 to the number of login attempts.
        """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """
        Reset the number of attempted logins to 0.

        :return: Sets the number of login attempts to 0.
        """
        self.login_attempts = 0
