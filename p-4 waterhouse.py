products = ["Laptop", "Keyboard", "Mouse", "Monitor"]

opening_stock = []
incoming_stock = []
dispatched_stock = []
actual_closing_stock = []

n = len(products)

print("WAREHOUSE INVENTORY RECONCILIATION")
print("-" * 40)

for i in range(n):
    print("\nProduct:", products[i])

    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    closing = int(input("Enter actual closing stock: "))

    if opening < 0 or incoming < 0 or dispatched < 0 or closing < 0:
        print("Invalid stock quantity! Enter non-negative values.")
        raise SystemExit

    if dispatched > opening + incoming:
        print("Error: Dispatch quantity exceeds available stock.")
        raise SystemExit

    opening_stock.append(opening)
    incoming_stock.append(incoming)
    dispatched_stock.append(dispatched)
    actual_closing_stock.append(closing)


print("\n========== INVENTORY REPORT ==========")

for i in range(n):
    expected_closing = (
        opening_stock[i]
        + incoming_stock[i]
        - dispatched_stock[i]
    )

    difference = actual_closing_stock[i] - expected_closing

    print("\nProduct:", products[i])
    print("Opening Stock:", opening_stock[i])
    print("Incoming Stock:", incoming_stock[i])
    print("Dispatched Stock:", dispatched_stock[i])
    print("Expected Closing Stock:", expected_closing)
    print("Actual Closing Stock:", actual_closing_stock[i])

    if difference == 0:
        print("Status: Stock Matched")
    elif difference < 0:
        print("Status: Stock Shortage =", abs(difference))
    else:
        print("Status: Stock Surplus =", difference)


    minimum_stock = 10

    if actual_closing_stock[i] < minimum_stock:
        replenishment = minimum_stock - actual_closing_stock[i]
        print("Replenishment Required:", replenishment)
    else:
        print("Replenishment Required: 0")
