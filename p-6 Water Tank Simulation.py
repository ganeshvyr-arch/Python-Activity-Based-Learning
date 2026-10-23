#python
# Multi-Day Water Tank Simulation

capacity = float(input("Enter tank capacity in litres: "))
water_level = float(input("Enter initial water level in litres: "))
threshold = float(input("Enter target water level in litres: "))
days = int(input("Enter number of days: "))

# Validate inputs
if capacity <= 0:
    print("Invalid tank capacity!")

elif water_level < 0 or water_level > capacity:
    print("Invalid initial water level!")

elif threshold < 0 or threshold > capacity:
    print("Invalid target water level!")

elif days <= 0:
    print("Number of days must be positive!")

else:
    first_threshold_day = -1
    overflow_count = 0
    shortage_count = 0

    print("\n===== WATER TANK REPORT =====")

    for day in range(1, days + 1):
        print("\nDay", day)

        inflow = float(input("Enter water inflow in litres: "))
        outflow = float(input("Enter water outflow in litres: "))

        if inflow < 0 or outflow < 0:
            print("Invalid inflow or outflow!")
            raise SystemExit

        # Calculate water level before applying capacity limits
        new_level = water_level + inflow - outflow

        # Detect overflow
        if new_level > capacity:
            print("Overflow detected!")
            overflow_count += 1
            new_level = capacity

        # Detect shortage
        if new_level < 0:
            print("Water shortage detected!")
            shortage_count += 1
            new_level = 0

        water_level = new_level

        print("Water level at end of day:", water_level, "litres")

        # Find the first day the threshold is reached
        if water_level >= threshold and first_threshold_day == -1:
            first_threshold_day = day
            print("Target water level reached on day", day)

    print("\n===== FINAL SUMMARY =====")
    print("Final water level:", water_level, "litres")
    print("Overflow incidents:", overflow_count)
    print("Shortage incidents:", shortage_count)

    if first_threshold_day != -1:
        print("First day target reached:", first_threshold_day)
    else:
        print("Target water level was not reached.")
