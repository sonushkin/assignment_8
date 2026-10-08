name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name:", name)
print("Next year you will be:", age + 1)
print("Height in cm:", height * 100)

if age < 0 or height < 0:
    print("Error: Age and height must be non-negative.")

quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_percent = float(input("Enter discount percent: "))

total = quantity * price
discount = total * discount_percent / 100
total_w_disc = total - discount

if quantity < 0 or price < 0 or discount_percent < 0:
    print("Error: Quantity, price, and discount percent must be non-negative.")

print("Total:", round(total, 3))
print("Discount:", round(discount, 3))
print("Total with discount:", round(total_w_disc, 3))

text = "My World. Nice World. A happy World! Indeed."
print(text)

index1 = text.find("World")
index2 = text.find("World", 9)

print("First World:", index1)
print("World after index 9:", index2)


last_index = text.rfind("World")
limited_index = text.rfind("World", 0, 25)
missing_index = text.rfind("Java")

print("Last World:", last_index)
print("Last World between indexes 0 and 25:", limited_index)
print("Last Java:", missing_index)

print(text[3]*2 + " Chat")
