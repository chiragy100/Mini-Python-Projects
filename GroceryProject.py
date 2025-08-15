items_dict = {"apple": 0.50, "banana": 0.30, "milk": 1.20, "bread": 1.00, "egg": 2.00}

cart = {}

print("Welcome to Python Grocery Store")
print("--------------------------------")

print("1. View available items")
print("2. Add item to cart")
print("3. View cart")
print("4. Remove item from cart")
print("5. Checkout")
print("6. Quit")

while True:
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 1:
        print("Available Options:")
        for item, price in items_dict.items():
            print(f"{item.title()}: ${price:.2f}")
    elif option == 2:
        order = str(input("Enter Item Name: "))
        if order in items_dict:
            quantity = int(input("Enter Quantity: "))
            cart.update([(order, quantity)])
            print(f"{quantity} {order}(s) added to your cart.")
        else:
            print("Invalid Item")
    elif option == 3:
        print("Your Cart: ")
        total = 0
        for order, quantity in cart.items():
            price = quantity * items_dict[order]
            total += price
            print(f"{order.title()} (x{quantity}): ${price:.2f}")
        print(f"Total: ${total:.2f}")
    elif option == 4:
        quit()

