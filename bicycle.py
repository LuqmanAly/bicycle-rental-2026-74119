
from rental_item import RentalItem


class Bicycle(RentalItem):
    def __init__(self, item_id, name, price_per_hour, bicycle_type):
        super().__init__(item_id, name, price_per_hour)

        if not isinstance(bicycle_type, str) or not bicycle_type.strip():
            raise ValueError("Bicycle type must be a non-empty string.")

        self.bicycle_type = bicycle_type

    def borrow(self):
        if not self.is_available:
            raise RuntimeError("Bicycle is already borrowed.")

        self.is_available = False
        return True

    def return_item(self):
        if self.is_available:
            raise RuntimeError("Bicycle has not been borrowed.")

        self.is_available = True
        return True

    @classmethod
    def from_dictionary(cls, data):
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        try:
            return cls(
                data["item_id"],
                data["name"],
                data["price_per_hour"],
                data["bicycle_type"]
            )
        except KeyError as error:
            raise ValueError(
                "Missing required field: " + str(error)
            ) from error

    @classmethod
    def from_hourly_rate(cls, item_id, name, hourly_rate, bicycle_type):
        return cls(item_id, name, hourly_rate, bicycle_type)

    def display_details(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Borrowed"

        print(
            "ID:", self.item_id,
            "| Name:", self.name,
            "| Type:", self.bicycle_type,
            "| Price/hour:", self.price_per_hour,
            "| Status:", status
        )
