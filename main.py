
from bicycle import Bicycle


def main():
    # Four bicycle objects
    bicycle1 = Bicycle("1", "Mountain Bike", 200, "Mountain")
    bicycle2 = Bicycle("2", "Road Bike", 150, "Road")
    bicycle3 = Bicycle("3", "Electric Bike", 350, "Electric")

    bicycle4 = Bicycle.from_dictionary({
        "item_id": "4",
        "name": "City Bike",
        "price_per_hour": 100,
        "bicycle_type": "City"
    })

    bicycles = [bicycle1, bicycle2, bicycle3, bicycle4]

    print("*=== Bicycle Rental System ===*")

    for bicycle in bicycles:
        bicycle.display_details()

    print("\n*=== Successful Operations ===*")

    bicycle1.borrow()
    print(bicycle1.name, "borrowed successfully.")

    print(
        "Rental cost for 3 hours:",
        bicycle1.calculate_rental_cost(3)
    )

    bicycle1.return_item()
    print(bicycle1.name, "returned successfully.")

    bicycle2.update_price(175)
    print("Updated road bike price:", bicycle2.price_per_hour)

    bicycle3.borrow()
    print(bicycle3.name, "borrowed successfully.")
    bicycle3.return_item()

    print("\n*=== Unsuccessful Operations ===*")

    try:
        bicycle1.return_item()
    except RuntimeError as error:
        print("Return error:", error)

    try:
        bicycle2.borrow()
        bicycle2.borrow()
    except RuntimeError as error:
        print("Borrow error:", error)

    try:
        bicycle2.calculate_rental_cost(-2)
    except ValueError as error:
        print("Rental duration error:", error)

    try:
        bicycle2.update_price(-50)
    except ValueError as error:
        print("Price error:", error)

    print("\n*=== Final Bicycle Status ===*")

    for bicycle in bicycles:
        bicycle.display_details()


if __name__ == "__main__":
    main()
