print("===== SMART PARKING SYSTEM =====")
print("1. Two-wheeler - Rs. 20 per hour")
print("2. Car          - Rs. 40 per hour")
print("3. Bus          - Rs. 60 per hour")

vehicle = int(input("Select vehicle category (1-3): "))

entry_hour = int(input("Enter entry hour (0-23): "))
entry_minute = int(input("Enter entry minute (0-59): "))

exit_hour = int(input("Enter exit hour (0-23): "))
exit_minute = int(input("Enter exit minute (0-59): "))


if vehicle < 1 or vehicle > 3:
    print("Invalid vehicle category.")

elif (entry_hour < 0 or entry_hour > 23 or
      exit_hour < 0 or exit_hour > 23 or
      entry_minute < 0 or entry_minute > 59 or
      exit_minute < 0 or exit_minute > 59):

    print("Invalid time entered.")

else:
    entry_time = entry_hour * 60 + entry_minute
    exit_time = exit_hour * 60 + exit_minute

    if exit_time < entry_time:
        duration = (1440 - entry_time) + exit_time
        overnight = True
    else:
        duration = exit_time - entry_time
        overnight = False

    parking_hours = duration // 60

    if duration % 60 != 0:
        parking_hours += 1

    if parking_hours == 0:
        parking_hours = 1

    if vehicle == 1:
        rate = 20
        vehicle_name = "Two-wheeler"
    elif vehicle == 2:
        rate = 40
        vehicle_name = "Car"
    else:
        rate = 60
        vehicle_name = "Bus"

    fee = parking_hours * rate

    if overnight:
        fee += 100

    daily_limit = 500

    if fee > daily_limit:
        fee = daily_limit

    print("\n===== PARKING BILL =====")
    print("Vehicle Type:", vehicle_name)
    print("Parking Duration:", duration, "minutes")
    print("Chargeable Hours:", parking_hours)
    print("Overnight Parking:", "Yes" if overnight else "No")
    print("Parking Fee: Rs.", fee)
