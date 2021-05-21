available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please input a direction: ").casefold()
    #CASEFOLD to tackle the CAPITAL LETTERS and mixed letters
    #   The person can quit the game if he wants to. So, we add it:
    if chosen_exit == "quit":
        print("Game Over")
        break

print("Aren't you glad you got out of there....")