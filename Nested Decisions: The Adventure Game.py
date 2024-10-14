# /// Task 1: Code Correction 
# You are provided with a Python script that is supposed to guide a user through an adventure game, 
# but it has some errors. Identify and fix them.


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

#  Task 2: Setting the SceneBased on your corrected code from Task 1,expand the game. 
# If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark",
#  and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")
light_options = input("light torch/proceed in the dark:")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print(light_options)
if light_options == "light torch":
    print("Torch Lit! You should see the hidden treasure clearly")
elif light_options == "proceed in the dark":
    print("Proceed in thr dark and feel your way to the treasure!")

# Task 3: Default Path If the user makes an invalid choice at any point,
#  incorporate a pass statement to handle it. HINT: How can an else statement be of use here?

place = input("Choose a place: forest or cave? ")
light_options = input("light torch/proceed in the dark:")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print(light_options)
if light_options == "light torch":
    print("Torch Lit! You should see the hidden treasure clearly")
elif light_options == "proceed in the dark":
    print("Proceed in thr dark and feel your way to the treasure!")
else:
    pass



