films = {

    "Black Panther 2": [13,10],
    "Everything, Everywhere, All At Once": [17,12],
    "Cinderella": [7,9],
    "Mr. Magoo": [3,1]

    }

while True:
    choice = input("Which film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        if age >= films[choice][0]:

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry, we are sold out.")

        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")
