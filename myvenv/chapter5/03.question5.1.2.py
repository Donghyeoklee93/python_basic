hour_of_studying = input("Enter the hour of studying >>>")
if int(hour_of_studying) >= 10:
    print("The phone's lock will be unlocked.")
elif int(hour_of_studying) >= 5:
    print("Using phone for 30 minutes is available.")
else:
    print("Using phone is not available.")