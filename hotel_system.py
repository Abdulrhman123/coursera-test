hotels = {
    "Nile Hotel": {"rooms": 5, "bookings": {}},
    "Sea View": {"rooms": 3, "bookings": {}},
    "Desert Inn": {"rooms": 4, "bookings": {}},
}


def choose_hotel():
    names = list(hotels)
    for i, hotel_name in enumerate(names, start=1):
        print(f"{i}. {hotel_name}")
    choice = input("choose hotel number: ")
    if choice.isdigit() and 1 <= int(choice) <= len(names):
        return names[int(choice) - 1]
    print("wrong choice")
    return None


def free_rooms(hotel_name):
    hotel = hotels[hotel_name]
    return [r for r in range(1, hotel["rooms"] + 1) if r not in hotel["bookings"]]


def show_hotels():
    print("\n--- hotels ---")
    for hotel_name, hotel in hotels.items():
        free = len(free_rooms(hotel_name))
        status = "available" if free > 0 else "full"
        print(f"{hotel_name}: {hotel['rooms']} rooms, {free} free ({status})")


def show_available_hotels():
    print("\n--- available hotels ---")
    found = False
    for hotel_name in hotels:
        free = free_rooms(hotel_name)
        if free:
            print(f"{hotel_name}: free rooms {free}")
            found = True
    if not found:
        print("all hotels are full")


def book_room():
    hotel_name = choose_hotel()
    if hotel_name is None:
        return
    free = free_rooms(hotel_name)
    if not free:
        print("sorry, this hotel is full")
        return
    print("free rooms:", free)
    room = input("choose room number: ")
    if not room.isdigit() or int(room) not in free:
        print("this room is not available")
        return
    name = input("what is your name: ")
    phone = input("what is your phone number: ")
    date = input("when do you want the room: ")
    hotels[hotel_name]["bookings"][int(room)] = {"name": name, "phone": phone, "date": date}
    print(f"done! room {room} in {hotel_name} is booked for {name}")


def show_bookings():
    print("\n--- bookings ---")
    found = False
    for hotel_name, hotel in hotels.items():
        for room, b in sorted(hotel["bookings"].items()):
            print(f"{hotel_name} - room {room}: {b['name']}, {b['phone']}, {b['date']}")
            found = True
    if not found:
        print("no bookings yet")


def cancel_booking():
    hotel_name = choose_hotel()
    if hotel_name is None:
        return
    room = input("room number to cancel: ")
    bookings = hotels[hotel_name]["bookings"]
    if room.isdigit() and int(room) in bookings:
        del bookings[int(room)]
        print("booking cancelled")
    else:
        print("this room is not booked")


print("Welcome to the Hotel Reservation System!")
while True:
    print("\n1. show all hotels")
    print("2. show available hotels and rooms")
    print("3. book a room")
    print("4. show bookings")
    print("5. cancel booking")
    print("6. exit")
    main_menu = input("choose: ")

    if main_menu == "1":
        show_hotels()
    elif main_menu == "2":
        show_available_hotels()
    elif main_menu == "3":
        book_room()
    elif main_menu == "4":
        show_bookings()
    elif main_menu == "5":
        cancel_booking()
    elif main_menu == "6":
        print("thank you")
        break
    else:
        print("wrong choice, try again")
