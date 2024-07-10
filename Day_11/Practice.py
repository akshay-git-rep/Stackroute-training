class Product:
    def __init__(self, device_name, price):
        self.name = device_name
        self.price = price
 
    def get_price(self):
        return self.price
 
class ElectronicDevice(Product):
    def __init__(self, name, brand, price):
        super().__init__(name, price)
        self.brand = brand
 
class Order:
    def __init__(self, items):
        self.items = items
        self.total_price = self.calculate_total_price()
 
    def calculate_total_price(self):
        total = sum(item.get_price() for item in self.items)
        return total
 
def write_order_to_file(order, file_name):
    with open(file_name, 'w') as file:
        file.write("Order Items:\n")
        for item in order.items:
            file.write(f"  - {item.name} ({item.brand}) - ${item.price:.2f}\n")
        file.write(f"Total Price: ${order.total_price:.2f}\n")
 
#   INPUTS
device1 = ElectronicDevice("Mobile", "Sony", 1052.10)
device2 = ElectronicDevice("Phone", "MI", 1609.00)
device3 = ElectronicDevice("Laptop", "HP", 9800.99)
device4 = ElectronicDevice("Laptop", "DELL", 9999.00)
 
 
order_items = [device1, device2,device3,device4]
my_order = Order(order_items)
 
# Writing to O/P file
write_order_to_file(my_order, "order_detail.txt")