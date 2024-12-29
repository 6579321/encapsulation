# Parent class Vehicle
class Vehicle:
    def __init__(self, vehicle_type, capacity):
        self.vehicle_type = vehicle_type
        self.capacity = capacity

    def get_vehicle_info(self):
        return f"Vehicle Type: {self.vehicle_type}, Capacity: {self.capacity}"

# Child class Bus inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self, vehicle_type, capacity, fare_per_passenger):
        # Initialize the parent class
        super().__init__(vehicle_type, capacity)
        self.fare_per_passenger = fare_per_passenger

    def calculate_total_fare(self, number_of_passengers):
        if number_of_passengers > self.capacity:
            return "Error: Number of passengers exceeds bus capacity!"
        return self.fare_per_passenger * number_of_passengers

# Example usage:
bus = Bus("City Bus", 50, 2.5)  # Bus with a capacity of 50 and fare of 2.5 per passenger

# Calculate fare for 30 passengers
number_of_passengers = 30
total_fare = bus.calculate_total_fare(number_of_passengers)

print(bus.get_vehicle_info())  # Print vehicle details
print(f"Total Fare for {number_of_passengers} passengers: ${total_fare}")
