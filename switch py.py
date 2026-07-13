def handle_choice(choice):
    match choice:
        case 1:
            print("You chose option 1")
        case 2:
            print("You chose option 2")
        case 3:
            print("You chose option 3")
        case _:
            print("Invalid choice")


handle_choice(3)