class Vehicle:
    def __init__(self):
        self.engine = False  # OFF
        self.doors = ["CLOSED"] * 4
        self.lights = ["OFF"] * 4

    # START ENGINE
    def start_engine(self):
        if self.engine:
            print("Engine is already running.")
            return

        open_doors = []
        for i in range(4):
            if self.doors[i] == "OPEN":
                open_doors.append(f"Door {i+1}")

        if open_doors:
            print("Cannot start engine. Open doors:", ", ".join(open_doors))
        else:
            self.engine = True
            print("Engine started successfully. Have a safe journey!")

    # STOP ENGINE
    def stop_engine(self):
        if not self.engine:
            print("Engine is already OFF.")
            return

        self.engine = False
        print("Engine stopped successfully.")

        on_lights = []
        for i in range(4):
            if self.lights[i] == "ON":
                on_lights.append(f"Light {i+1}")

        if on_lights:
            print("Warning: Lights still ON ->", ", ".join(on_lights))

    # VIEW STATUS
    def view_status(self):
        print("\n===== VEHICLE STATUS =====")

        print("Engine:", "RUNNING" if self.engine else "OFF")

        for i in range(4):
            print(f"Door {i+1}: {self.doors[i]}")

        for i in range(4):
            print(f"Light {i+1}: {self.lights[i]}")


# ---------------- MAIN PROGRAM ----------------

vehicle = Vehicle()

while True:
    print("\n===== MAIN MENU =====")
    print("1. Set Door Status")
    print("2. Set Light Status")
    print("3. Start Engine")
    print("4. Stop Engine")
    print("5. View Vehicle Status")
    print("6. Exit")

    choice = input("Enter choice: ")

    # SET DOOR STATUS
    if choice == "1":
        door = int(input("Door number (1-4): "))
        status = input("OPEN/CLOSED: ").upper()

        if 1 <= door <= 4:
            vehicle.doors[door - 1] = status
        else:
            print("Invalid door number")

    # SET LIGHT STATUS
    elif choice == "2":
        light = int(input("Light number (1-4): "))
        status = input("ON/OFF: ").upper()

        if 1 <= light <= 4:
            vehicle.lights[light - 1] = status
        else:
            print("Invalid light number")

    # START ENGINE
    elif choice == "3":
        vehicle.start_engine()

    # STOP ENGINE
    elif choice == "4":
        vehicle.stop_engine()

    # VIEW STATUS
    elif choice == "5":
        vehicle.view_status()

    # EXIT
    elif choice == "6":
        print("Exiting...")
        break

    # INVALID INPUT
    else:
        print("Invalid choice. Try again.")