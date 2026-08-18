print("\n--- MINI SHOPPING CART ---")

products = ["Rice", "Bread", "Milk", "Wheat"]
prices = [25, 20, 30, 80]

cart = []
total = 0

while True:
    print("\nAvailable Products:")

    for i in range(len(products)):
        print(i + 1, "-_", products[i], "- Rs", prices[i])

    print("5. Exit")

    try:
        choice = int(input("ENTER PRODUCT NO: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if 1 <= choice <= 4:
        product_index = choice - 1
        cart.append(products[product_index])
        total += prices[product_index]
        print(products[product_index], "ADDED TO CART")

    elif choice == 5:
        break

    else:
        print("INVALID CHOICE...")

print("\n--- YOUR CART ---")

if len(cart) == 0:
    print("Cart is empty")
else:
    for item in cart:
        print("-", item)

    print("Total Amount = Rs", total)

print("THANK YOU...")