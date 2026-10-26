products = ["Rice", "Sugar", "Oil", "Biscuits", "Milk"]
prices = [60, 45, 150, 30, 50]

quantities = []
total_cost = 0

budget = float(input("Enter your shopping budget (Rs.): "))

if budget <= 0:
    print("Invalid budget!")

print("\n===== SHOPPING BASKET =====")

for i in range(len(products)):
    print("\nProduct:", products[i])
    print("Price per unit: Rs.", prices[i])

    quantity = int(input("Enter quantity: "))

    if quantity < 0:
        print("Invalid quantity!")

    quantities.append(quantity)
    total_cost += prices[i] * quantity

if total_cost >= 2000:
    discount_rate = 10
elif total_cost >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = total_cost * discount_rate / 100
final_cost = total_cost - discount

print("\n===== BILL SUMMARY =====")
print("Total Cost: Rs.", round(total_cost, 2))
print("Discount Rate:", discount_rate, "%")
print("Discount Amount: Rs.", round(discount, 2))
print("Final Cost: Rs.", round(final_cost, 2))
print("Shopping Budget: Rs.", round(budget, 2))

if final_cost <= budget:
    print("Status: Shopping is within budget.")
else:
    print("Status: Shopping exceeds the budget.")

    excess = final_cost - budget
    print("Amount exceeding budget: Rs.", round(excess, 2))

    print("\n===== SUGGESTED QUANTITY REDUCTIONS =====")

    for i in range(len(products)):
        while quantities[i] > 0 and final_cost > budget:
            quantities[i] -= 1

            total_cost = 0
            for j in range(len(products)):
                total_cost += prices[j] * quantities[j]

            if total_cost >= 2000:
                discount_rate = 10
            elif total_cost >= 1000:
                discount_rate = 5
            else:
                discount_rate = 0

            discount = total_cost * discount_rate / 100
            final_cost = total_cost - discount

        if final_cost <= budget:
            break

    print("\n===== REVISED SHOPPING BASKET =====")

    for i in range(len(products)):
        print(products[i], ":", quantities[i], "units")

    print("Revised Total Cost: Rs.", round(total_cost, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Revised Final Cost: Rs.", round(final_cost, 2))

    if final_cost <= budget:
        print("Status: Shopping is now within budget.")
    else:
        print("Status: Budget cannot be met with the available products.")
