
from abc import ABC, abstractmethod


class RentalItem(ABC):
    def __init__(self, item_id, name, price_per_hour):
        if not isinstance(item_id, str) or not item_id.strip():
            raise ValueError("Item ID must be a non-empty string.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")

        if isinstance(price_per_hour, bool) or not isinstance(
            price_per_hour, (int, float)
        ):
            raise ValueError("Price must be a number.")

        if price_per_hour < 0:
            raise ValueError("Price cannot be negative.")

        self.item_id = item_id
        self.name = name
        self.price_per_hour = float(price_per_hour)
        self.is_available = True

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    def calculate_rental_cost(self, hours):
        if isinstance(hours, bool) or not isinstance(hours, (int, float)):
            raise ValueError("Hours must be a number.")

        if hours <= 0:
            raise ValueError("Hours must be greater than zero.")

        return self.price_per_hour * hours

    def update_price(self, new_price):
        if isinstance(new_price, bool) or not isinstance(
            new_price, (int, float)
        ):
            raise ValueError("Price must be a number.")

        if new_price < 0:
            raise ValueError("Price cannot be negative.")

        self.price_per_hour = float(new_price)

    @classmethod
    def from_dictionary(cls, data):
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        try:
            return cls(
                data["item_id"],
                data["name"],
                data["price_per_hour"]
            )
        except KeyError as error:
            raise ValueError(
                "Missing required field: " + str(error)
            ) from error
