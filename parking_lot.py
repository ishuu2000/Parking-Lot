class ParkingLot:
    def __init__(self, levels, capacity_per_level):
        self.levels = levels
        self.capacity_per_level = capacity_per_level
        self.parking_spots = {level: set(range(1, capacity_per_level + 1)) for level in levels}
        self.occupied_spots = {}  # {vehicle_number: (level, spot_number)}

    def assign_parking_spot(self, vehicle_number):
        for level in self.levels:
            if self.parking_spots[level]:
                spot_number = self.parking_spots[level].pop()
                self.occupied_spots[vehicle_number] = (level, spot_number)
                return {"level": level, "spot": spot_number}

        return {"message": "Parking lot is full"}

    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.occupied_spots:
            level, spot_number = self.occupied_spots[vehicle_number]
            return {"level": level, "spot": spot_number}
        else:
            return {"message": "Vehicle not found"}

    def unpark_vehicle(self, vehicle_number):
        if vehicle_number in self.occupied_spots:
            level, spot_number = self.occupied_spots.pop(vehicle_number)
            self.parking_spots[level].add(spot_number)
            return {"message": "Vehicle unparked"}
        else:
            return {"message": "Vehicle not found"}

    def retrieve_nearest_parking_spot(self):
        for level in self.levels:
            if self.parking_spots[level]:
                spot_number = min(self.parking_spots[level])
                return {"level": level, "spot": spot_number}

        return {"message": "Parking lot is full"}


if __name__ == "__main__":
    parking_lot = ParkingLot(levels=["A", "B"], capacity_per_level=20)

    while True:
        print("\nOptions:")
        print("1. Assign Parking Spot")
        print("2. Retrieve Parking Spot")
        print("3. Unpark Vehicle")
        print("4. Retrieve Nearest Parking Spot")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.assign_parking_spot(vehicle_number)
            print(result)

        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(result)

        elif choice == "3":
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.unpark_vehicle(vehicle_number)
            print(result)

        elif choice == "4":
            result = parking_lot.retrieve_nearest_parking_spot()
            print(result)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
