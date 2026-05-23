signal = input("Enter traffic signal color (red/yellow/green): ")

if signal.lower() == "red":
    print("STOP")
elif signal.lower() == "yellow":
    print("READY")
elif signal.lower() == "green":
    print("GO")
else:
    print("Invalid Signal")