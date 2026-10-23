# Attendance Recovery Computation

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
required_percentage = float(input("Enter required attendance percentage: "))

# Validate input
if total_classes < 0 or attended_classes < 0:
    print("Invalid input! Class counts cannot be negative.")

elif attended_classes > total_classes:
    print("Invalid input! Attended classes cannot exceed total classes.")

elif required_percentage < 0 or required_percentage > 100:
    print("Invalid attendance percentage!")

else:
    # Calculate current attendance percentage
    if total_classes == 0:
        current_percentage = 0
    else:
        current_percentage = (attended_classes / total_classes) * 100

    print("\n--- Attendance Report ---")
    print("Total classes conducted:", total_classes)
    print("Classes attended:", attended_classes)
    print("Current attendance:", round(current_percentage, 2), "%")
    print("Required attendance:", required_percentage, "%")

    if current_percentage >= required_percentage:
        print("Status: Eligible for examination")
        print("Additional consecutive classes required: 0")

    else:
        # Calculate minimum consecutive classes to attend
        future_classes = 0

        while True:
            future_percentage = (
                (attended_classes + future_classes)
                / (total_classes + future_classes)
            ) * 100

            if future_percentage >= required_percentage:
                break

            future_classes += 1

        print("Status: Not currently eligible")
        print("Minimum consecutive classes to attend:", future_classes)

        # Show future attendance scenarios
        print("\n--- Future Attendance Scenarios ---")

        for extra_classes in [5, 10, 15, 20]:
            future_attendance = (
                (attended_classes + extra_classes)
                / (total_classes + extra_classes)
            ) * 100

            print(
                "After attending", extra_classes,
                "consecutive classes:",
                round(future_attendance, 2), "%"
            )