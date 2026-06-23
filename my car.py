doors = "closed"
lights = "off"
engine = "off"

while True:

    print("--- CAR STATUS ---")
    print("Engine:", engine)
    print("Doors:", doors)
    print("Lights:", lights)

    print("1. Set Door Status")
    print("2. Set Light Status")
    print("3. Start Engine")
    print("4. Stop Engine")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        doors = input("Enter door status OPEN/CLOSED: ")

        if doors == "open" or doors == "closed":
            print("Door status changed")
        else:
            print("Invalid door status")


    elif choice == "2":
        lights = input("Enter light status ON/OFF: ")

        if lights == "on" or lights == "off":
            print("Light status changed")
        else:
            print("Invalid light status")


    elif choice == "3":

        if engine == "running":
            print("Engine already running")

        elif doors == "open":
            print("Cannot start.stupid Door is open")

        else:
            engine = "running"
            print("Engine started")


    elif choice == "4":

        if engine == "off":
            print("Engine already OFF")

        elif lights == "on":
            engine = "off"
            print("Engine stopped")
            print("Warning: Lights are ON")

        else:
            engine = "off"
            print("Engine stopped successfully")


    elif choice == "5":
        print("Exit")
        break


    else:
        print("wrong option selected")