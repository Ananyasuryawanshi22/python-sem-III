import json

FILE = "drivers.json"


# Load drivers from JSON file
def load_drivers():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save drivers to JSON file
def save_drivers(drivers):
    with open(FILE, "w") as file:
        json.dump(drivers, file, indent=4)


# 1. Add driver
def add_driver():
    drivers = load_drivers()

    driver = {
        "id": int(input("Enter Driver ID: ")),
        "name": input("Enter Driver Name: "),
        "mobile": input("Enter Mobile Number: "),
        "cab_number": input("Enter Cab Number: "),
        "cab_type": input("Enter Cab Type: "),
        "experience": int(input("Enter Experience (years): ")),
        "rating": float(input("Enter Rating: ")),
        "available": input("Is driver available? (yes/no): ").lower()
    }

    drivers.append(driver)
    save_drivers(drivers)

    print("Driver added successfully!")


# 2. Display all drivers
def display_drivers():
    drivers = load_drivers()

    if not drivers:
        print("No drivers found.")
        return

    for driver in drivers:
        print("\nDriver ID:", driver["id"])
        print("Name:", driver["name"])
        print("Mobile:", driver["mobile"])
        print("Cab Number:", driver["cab_number"])
        print("Cab Type:", driver["cab_type"])
        print("Experience:", driver["experience"], "years")
        print("Rating:", driver["rating"])
        print("Availability:", driver["available"])


# 3. Search driver by ID
def search_driver():
    drivers = load_drivers()
    driver_id = int(input("Enter Driver ID to search: "))

    for driver in drivers:
        if driver["id"] == driver_id:
            print("\nDriver Found")
            print(driver)
            return

    print("Driver not found.")


# 4. Update driver availability
def update_availability():
    drivers = load_drivers()
    driver_id = int(input("Enter Driver ID: "))

    for driver in drivers:
        if driver["id"] == driver_id:
            driver["available"] = input("Enter availability (yes/no): ").lower()
            save_drivers(drivers)
            print("Availability updated successfully!")
            return

    print("Driver not found.")


# 5. Search drivers with rating above given value
def search_by_rating():
    drivers = load_drivers()
    rating = float(input("Enter rating value: "))

    found = False

    for driver in drivers:
        if driver["rating"] > rating:
            print("\nID:", driver["id"])
            print("Name:", driver["name"])
            print("Rating:", driver["rating"])
            found = True

    if not found:
        print("No drivers found.")


# 6. Delete driver
def delete_driver():
    drivers = load_drivers()
    driver_id = int(input("Enter Driver ID to delete: "))

    for driver in drivers:
        if driver["id"] == driver_id:
            drivers.remove(driver)
            save_drivers(drivers)
            print("Driver deleted successfully!")
            return

    print("Driver not found.")


# 7. Display available drivers
def display_available():
    drivers = load_drivers()

    print("\nAvailable Drivers:")

    found = False

    for driver in drivers:
        if driver["available"] == "yes":
            print("ID:", driver["id"])
            print("Name:", driver["name"])
            print("Cab Number:", driver["cab_number"])
            print("Cab Type:", driver["cab_type"])
            print("Rating:", driver["rating"])
            print()
            found = True

    if not found:
        print("No drivers are available.")


# Main menu
while True:
    print("\n===== CAB DRIVER MANAGEMENT SYSTEM =====")
    print("1. Add Driver")
    print("2. Display All Drivers")
    print("3. Search Driver by ID")
    print("4. Update Driver Availability")
    print("5. Search Drivers by Rating")
    print("6. Delete Driver")
    print("7. Display Available Drivers")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_driver()

    elif choice == "2":
        display_drivers()

    elif choice == "3":
        search_driver()

    elif choice == "4":
        update_availability()

    elif choice == "5":
        search_by_rating()

    elif choice == "6":
        delete_driver()

    elif choice == "7":
        display_available()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")