"""A class to represent an administrative user."""
from barcalow_user import User

class Privileges:
    """A class to describe a list of privileges that a user has."""

    def __init__(self, user_name: str, privileges: list):
        """
        Initialize the privileges available.

        :param privileges: List of privileges available to a user.
        """
        self.user_name = user_name
        self.privileges = privileges

    def show_privileges(self):
        """
        Print the user's privileges.

        :return: Prints a list of items in the privilege list.
        """
        print(f"{self.user_name} can:")
        for priv in self.privileges:
            print("  -", priv)


class Admin(User):
    """A super-user who can do more things than a regular user."""
    def __init__(self, first_name: str, last_name: str, age: int,
                 location: str, pronouns: list = None):
        super().__init__(first_name, last_name, age, location, pronouns)
        self.privileges = Privileges(f"{self.first_name} {self.last_name}", [
            "add post",
            "delete post",
            "ban user",
            "delete comment",
        ])
