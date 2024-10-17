"""Write Python classes to represent Apartment, Building, and Villa.

[X] The class Asset has a name, address, and revenue as attributes, where
    revenue is a float value.
[X] Building and Villa inherit from the class Asset.
    [X] A Villa is an Asset that has rent and maintenance, both are float
        values.
    [X] A Building is an Asset that has a number of apartments.
    [X] An Apartment has rent and maintenance, both are float values.
[X] All the revenue and rent attributes are private.
[X] Each class has a revenue() method to calculate the monthly revenue as
    shown below.
[X] Your program needs to calculate the revenue from Buildings and Villas and
    display the Asset's name, address, and total revenue.
[X] Test the program to display the details of all assets. If a particular
    asset does not generate any revenue, an appropriate exception is thrown to
    indicate the same.

Formulas:

Villa Revenue = rent – maintenance
Building Revenue = (apartments * apartment rent) – (maintenance * apartments)

[X] The student is required to identify classes, related attributes, and
    behaviors.
[X] Students are free to add as many attributes as required.
[X] The appropriate access modifiers (private, public, or protected) must be
    used while implementing class relationships.
[X] Proper documentation of code is mandatory.
[X] The student must also test the code by creating at least three objects.
[X] All classes must have a display function, and the program must have the
    functionality to print the current state of the objects.
"""

class Asset:
    """Represents a revenue-generating asset."""

    def __init__(self, name: str, address: str):
        """
        Initialize the asset's name, address, revenue, and type (so that the
        __str__ method doesn't print <class '__main__.Type'> but just prints
        the type).

        :param name: Name of the asset.
        :param address: Street address of the asset.
        """
        self.name = name
        self.address = address
        self.__revenue = 0.0
        self.type = "asset"

    def __str__(self):
        """
        Print a statement of the asset's name and address.

        :return: Returns a string with the asset's name and address.
        """
        return f"The {self.type} {self.name} is located at {self.address}."

    def __repr__(self):
        """
        Provide a call that could instantiate an identical instance.

        :return: Returns the necessary call to create an Asset with the same
            base properties.
        """
        return f"Asset({repr(self.name)}, {repr(self.address)})"

    @property
    def revenue(self):
        """
        Return the revenue of the asset. This will be overwritten in the
        subclasses.

        :return: In Asset, returns the revenue value with a dollar sign.
        """
        if self.__revenue <= 0:
            return f"{self.name} does not generate any monthly revenue."
        return f"{self.name}'s monthly revenue is ${self.__revenue:.2f}"


class Villa(Asset):
    """A type of asset that has rent and requires maintenance."""
    def __init__(self, name: str, address: str, rent: float, maint: float):
        """
        Initialize the villa with a name, address, rent cost, and maintenance
        cost.

        :param name: Name of the villa.
        :param address: Street address of the villa.
        :param rent: Monthly rent cost (private).
        :param maint: Monthly maintenance cost (private).
        """
        super().__init__(name, address)
        # Note: These are private variables, but are defined at the start of
        # the program. In a real application, these would probably be pulled
        # from a database.
        self.__rent = rent
        self.__maint = maint
        self.type = "villa"

    def __repr__(self):
        """
        Provide a call that could instantiate an identical instance.

        :return: Returns the necessary call to create a Villa with the same
            base properties.
        """
        return (f"Villa({repr(self.name)}, {repr(self.address)}, "
                f"{repr(self.__rent)}, {repr(self.__maint)})")

    @property
    def revenue(self):
        """
        Generate the monthly revenue for a villa.

        Monthly revenue for a villa is (rent - maintenance).

        :return: In Villa, returns the difference between rent and maintenance
            with a dollar sign added.
        """
        self.__revenue = self.__rent - self.__maint
        if self.__revenue <= 0:
            return f"{self.name} does not generate any monthly revenue."
        return f"{self.name}'s monthly revenue is ${self.__revenue:.2f}"


class Apartment:
    """Represents a small living space inside a building."""

    def __init__(self, rent: float, maint: float):
        """
        Initialize the apartment's rent and maintenance costs.

        :param rent: Monthly rent cost (private).
        :param maint: Monthly maintenance cost (private).
        """
        self.__rent = rent
        self.__maint = maint

    def __str__(self):
        """
        Print a statement that this is an apartment. There is no name or
        address to represent, and the maintenance cost is private.

        :return: Returns the rent cost of the apartment.
        """
        return f"Apartment with a rent of ${self.__rent}"

    def __repr__(self):
        """
        Provide a call that could instantiate an identical instance.

        :return: Returns the necessary call to instantiate a new Apartment
            with the same properties.
        """
        return f"Apartment({self.__rent}, {self.__maint})"

    @property
    def rent(self):
        """
        Keep the rent private, but return the value.

        :return: Returns the rent.
        """
        return self.__rent

    @property
    def maint(self):
        """
        Keep the maintenance costs private, but return the value.

        :return: Returns the maintenance cost.
        """
        return self.__maint


class Building(Asset):
    """A building filled with apartments that can be rented."""

    def __init__(self, name: str, address: str, apartments: int, rent: float,
                 maint: float):
        """
        Initialize the building's name, address, number of apartments and cost
        of apartments, and type.

        :param name: Name of the building.
        :param address: Street address of the building.
        :param apartments: Number of apartments in the building.
        :param rent: Rent of one apartment.
        :param maint: Maintenance cost of one apartment.
        """
        super().__init__(name, address)
        self.apartments = apartments
        self.apartment = Apartment(rent, maint)
        self.type = "building"

    def __repr__(self):
        """
        Provide a call that could instantiate an identical instance.

        :return: Returns the necessary call to instantiate a new Building with
            the same properties.
        """
        return (f"Building({repr(self.name)}, {repr(self.address)}, "
                f"{repr(self.apartments)}, {repr(self.apartment.rent)}, "
                f"{repr(self.apartment.maint)})")

    @property
    def revenue(self):
        """
        Generate the monthly revenue for a building.

        Monthly revenue for a building is
        (apartments * rent) – (apartments * maintenance)

        :return: In Building, returns the difference between total rent and
            total maintenance with a dollar sign added.
        """
        self.__revenue = ((self.apartments * self.apartment.rent)
                         -(self.apartments * self.apartment.maint))
        if self.__revenue <= 0:
            return f"{self.name} does not generate any monthly revenue."
        return f"{self.name}'s monthly revenue is ${self.__revenue:.2f}"


vil = Villa("Merriweather Heights", "4425 Pork Avenue", 350, 145)

print(vil.revenue)
print(vil)
print(repr(vil))

print()

build = Building("Carlo Apartments", "1225 Monte Boulevard", 120, 250, 150)
print(build.revenue)
print(build)
print(repr(build))

print()

apart = Apartment(150, 120)
print(apart)

print()

startup = Building("Money Lounge", "4400 Marvin Gardens Avenue", 50, 100, 150)
print(startup.revenue)
print(startup)
print(repr(startup))

print()

lot = Asset("Vacant Lot", "6243 Plain Road")
print(lot.revenue)
print(lot)