class ride:

    def __init__(self, ride_id, from_where, to_destination, fare):
        self.ride_id = ride_id
        self.from_where = from_where
        self.to_destination = to_destination
        self.fare = fare

class driver:

    def __init__(self, name, car_number):
        self.name = name
        self.car_number = car_number
        self.ride = []
        self.total_ride = 0
        self.total_fare = 0

    def add_ride(self, ride):
        self.ride.append(ride)
        self.total_fare += ride.fare 
    
    def get_ride_count(self):
        return len(self.ride)
    
driver1 = driver(name="akshay", car_number="ka01mk7244")
driver2 = driver(name="bharath", car_number="ap05aa0000")

ride1 = ride(ride_id=1, from_where="cubbonpet", to_destination="white field", fare=50)
ride2 = ride(ride_id=2, from_where="bangalore", to_destination="yelanka", fare=40)
ride3 = ride(ride_id=3, from_where="gada", to_destination="badami", fare=100)

driver1.add_ride(ride1)
driver1.add_ride(ride2)
driver2.add_ride(ride3)

print("====================================")
print(f"Driver: {driver1.name}, Car Number: {driver1.car_number}")
print(f"Total rides: {driver1.get_ride_count()}, Total fare: ${driver1.total_fare}")

print("====================================")

print(f"Driver: {driver2.name}, Car Number: {driver2.car_number}")
print(f"Total rides: {driver2.get_ride_count()}, Total fare: ${driver2.total_fare}")
print("====================================")
