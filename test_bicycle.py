
import unittest

from abc import ABC
from bicycle import Bicycle
from rental_item import RentalItem


class TestBicycleRentalSystem(unittest.TestCase):

    def setUp(self):
        self.bicycle = Bicycle(
            "1", "Mountain Bike", 200, "Mountain"
        )

    # Test 1 where we will test object creation
    def test_bicycle_creation(self):
        self.assertEqual(self.bicycle.item_id, "1")
        self.assertEqual(self.bicycle.name, "Mountain Bike")
        self.assertEqual(self.bicycle.price_per_hour, 200.0)
        self.assertEqual(self.bicycle.bicycle_type, "Mountain")
        self.assertTrue(self.bicycle.is_available)

    # Test 2 is inheritance
    def test_inheritance(self):
        self.assertIsInstance(self.bicycle, RentalItem)

    # Test 3 Abstract base class
    def test_rental_item_is_abstract(self):
        self.assertTrue(issubclass(RentalItem, ABC))
        with self.assertRaises(TypeError):
            RentalItem("R1", "Item", 100)

    # Test 4 Successful borrowing
    def test_borrow_bicycle(self):
        self.bicycle.borrow()
        self.assertFalse(self.bicycle.is_available)

    # Test 5 Borrowing an unavailable bicycle
    def test_borrow_twice(self):
        self.bicycle.borrow()
        with self.assertRaises(RuntimeError):
            self.bicycle.borrow()

    # Test 6 Successful return
    def test_return_bicycle(self):
        self.bicycle.borrow()
        self.bicycle.return_item()
        self.assertTrue(self.bicycle.is_available)

    # Test 7 Returning without borrowing
    def test_return_without_borrowing(self):
        with self.assertRaises(RuntimeError):
            self.bicycle.return_item()

    # Test 8 Rental cost calculation
    def test_rental_cost(self):
        self.assertEqual(
            self.bicycle.calculate_rental_cost(3), 600.0
        )

    # Test 9 Invalid rental duration
    def test_invalid_rental_duration(self):
        with self.assertRaises(ValueError):
            self.bicycle.calculate_rental_cost(0)

    # Test 10 Negative rental duration
    def test_negative_rental_duration(self):
        with self.assertRaises(ValueError):
            self.bicycle.calculate_rental_cost(-2)

    # Test 11 Successful price update
    def test_update_price(self):
        self.bicycle.update_price(250)
        self.assertEqual(self.bicycle.price_per_hour, 250.0)

    # Test 12 Negative price update
    def test_negative_price(self):
        with self.assertRaises(ValueError):
            self.bicycle.update_price(-10)

    # Test 13 where we put empty bicycle ID
    def test_empty_id(self):
        with self.assertRaises(ValueError):
            Bicycle("", "Road Bike", 150, "Road")

    # Test 14 Negative initial price
    def test_negative_initial_price(self):
        with self.assertRaises(ValueError):
            Bicycle("2", "Road Bike", -100, "Road")

    # Test 15 Empty bicycle type
    def test_empty_bicycle_type(self):
        with self.assertRaises(ValueError):
            Bicycle("3", "Road Bike", 100, "")




if __name__ == "__main__":
    unittest.main()
