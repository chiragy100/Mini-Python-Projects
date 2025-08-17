"""
Python Grocery Store Simulation
-------------------------------
This program simulates a simple grocery shopping system where a user can:
1. View available items
2. Add items to their cart
3. View the cart with running totals
4. Remove items from the cart
5. Checkout using a valid checkout key
6. Quit the program

Concepts used:
- Dictionaries for item storage and cart tracking
- Loops and conditionals for menu navigation
- Functions for cart display
- Error handling using try/except
"""

# Dictionary storing available items and their prices
items_dict = {"apple": 0.50, "banana": 0.30, "milk": 1.20, "bread": 1.00, "egg": 2.00}

# Dictionary to hold user’s current cart (item -> quantity)
cart = {}

# Predefined valid checkout keys for transaction verification
valid_checkout = [7181984, 2181982, 6152009]


def cart_display():
    """
    Displays the current cart contents and calculates the total cost.
    Loops through each item in the cart, multiplies price by quantity,
    and prints item details with running total.
    """
    total = 0
    for order, quantity in cart.items():
        price = quantity * items_dict[order]
        total += price
        print(f"{order.title()} (x{quantity}): ${price:.2f}")
    print(f"Total: ${total:.2f}")


# Main menu
print("Welcome to Python Grocery Store")
print("--------------------------------")
print("1. View available items")
print("2. Add item to cart")
print("3. View cart")
print("4. Remove item from cart")
print("5. Checkout")
print("6. Quit")

# Main program loop
while True:
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        # Prevents crash if user enters non-numeric input
        print("Please enter a valid number.")
        continue

    # View available items
    if option == 1:
        print("Available Options:")
        for item, price in items_dict.items():
            print(f"{item.title()}: ${price:.2f}")

    # Add item to cart
    elif option == 2:
        order = str(input("Enter Item Name: ")).lower()
        if order in items_dict:
            quantity = int(input("Enter Quantity: "))
            # Add to cart or update existing quantity
            cart[order] = cart.get(order, 0) + quantity
            print(f"{quantity} {order}(s) added to your cart.")
        else:
            print("Invalid Item")

    # View cart
    elif option == 3:
        print("Your Cart: ")
        cart_display()

    # Remove item from cart
    elif option == 4:
        if not cart:
            print('Empty Cart')
        else:
            print("Your Cart: ")
            cart_display()

            remove = input("What items do you want to remove: ").lower()
            if remove in cart:
                cart.pop(remove)
                print("Updated Cart: ")
                cart_display()
            else:
                print("Item not in cart. ")

    # Checkout process
    elif option == 5:
        print("Cart: ")
        cart_display()

        co = input("Press x if you're ready to checkout: ").lower()
        if co == 'x':
            if not cart:
                print("Empty cart, cannot proceed.")
            else:
                checkout = int(input("Enter a valid key: "))
                if checkout in valid_checkout:
                    print("Transaction Successful!")
                    print("Thanks for shopping with us.")
                    quit()
                else:
                    print("Invalid Key.")
        else:
            print(" ")

    # Quit program
    elif option == 6:
        print("Goodbye!")
        quit()
