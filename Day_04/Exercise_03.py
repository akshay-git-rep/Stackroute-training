def generate_invoice(customer_name, items, tax_rate):
 
   print("============================================")
   print("Invoice")
   print("============================================")
   print(f"Customer Name: {customer_name}")
   print("Items")
   print("{:<15} {:<10} {:<8} {:<10}".format("Item Name", "Price", "Quantity", "Subtotal"))
   print("--------------------------------------")
   total_cost = 0
 
   for item in items:
       item_name, price, quantity = item
       item_cost = price * quantity
       total_cost += item_cost
       #print("{:<15} ${:<10} {:<8} ${:<10}".format(item_name, price, quantity, item_cost))
       print(f"{item_name:<15}  ${price:<10}  {quantity:<8}  ${item_cost:<10}")
 
 
   tax_amount = total_cost * tax_rate
   total_amount = total_cost + tax_amount
   print("--------------------------------------")
   print(f"Subtotal: ${total_cost:2}")
   print(f"Tax ({tax_rate*100}%): ${tax_amount:2}")
   print("--------------------------------------")
   print(f"Total: ${total_amount:2}")
   print("Thank you for your business!")
   print("============================================")
 
 
customer_name = "John Doe"
items = [("Computer", 1000.00, 1), ("Mouse", 20.00, 2)]
tax_rate = 0.07
 
generate_invoice(customer_name, items, tax_rate)