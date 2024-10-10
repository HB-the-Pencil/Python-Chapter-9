class Car:
    """Basic model for a car."""

    def __init__(self, make: str, model: str, year: int):
        """
        Initialize a car with details about its make.

        :param make: Manufacturer of the car (e.g. Honda).
        :param model: Model of the car (e.g. Civic).
        :param year: Year the car was made (e.g. 2011).
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_name(self):
        """
        Return a neatly formatted version of the car's name.

        :return: String of the car's name, formatted nicely.
        """
        return f"{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        """
        Read the car's odometer and print the mileage.

        :return: Prints the car's mileage.
        """
        print(f"This car has {self.odometer} miles on it.")

    def set_odometer(self, mileage):
        """
        Update the odometer after driving the car.

        :param mileage: Miles the odometer should read.
        :return: Updates odometer if the new distance is greater than the
            current distance. Otherwise, tell the user that you can't roll
            back an odometer.
        """
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def drive_car(self, distance: int):
        """
        Update the odometer after driving the car.

        :param distance: Distance driven (to the nearest mile).
        :return: Updates odometer if distance is positive. Otherwise, tell the
            user that you can't roll back an odometer.
        """
        if distance >= 0:
            self.odometer += distance
        else:
            print("You can't roll back an odometer!")


class Battery:
    """A battery for an electric vehicle."""

    def __init__(self, capacity = 40):
        """
        Initialize the battery with a capacity.

        :param capacity: How much energy the battery holds.
        """
        self.capacity = capacity

    def describe_battery(self):
        """
        Print the car's battery capacity.

        :return: Prints a statement about how much energy the battery holds.
        """
        print(f"This car has a {self.capacity}-kWh battery.")

    def describe_range(self):
        """
        Print the approximate range of the car's battery.

        :return: Prints a statement about the range of the battery.
        """
        if self.capacity == 40:
            drive_range = 150
        elif self.capacity == 65:
            drive_range = 225
        else:
            drive_range = 0

        if drive_range:
            print(f"This car can go about {drive_range} miles on a charge.")
        else:
            print("Specify battery size (40 kWh or 65 kWh).")

    def upgrade_battery(self):
        """
        Upgrade a car's battery size.

        :return: Prints a message with the car's updated battery size.
        """
        if self.capacity != 65:
            self.capacity = 65
            print("Your car's battery capacity is now 65 kWh!")
        else:
            print("Your car's battery capacity is already 65 kWh!")


class ElectricCar(Car):
    """An electric version of a car."""

    def __init__(self, make: str, model: str, year: int):
        """
        Initialize the car according to the parent function.

        :param make: Manufacturer of the car (e.g. Nissan).
        :param model: Model of the car (e.g. Leaf).
        :param year: Year the car was made.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


electric = ElectricCar("Nissan", "Leaf", 2024)
print(electric.get_name())
electric.battery.describe_battery()
electric.battery.describe_range()
electric.battery.upgrade_battery()
electric.battery.describe_range()