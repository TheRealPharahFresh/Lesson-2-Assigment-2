# Task 1: Code Correction 
# You are provided with a Python script that is supposed to help in event planning,
#  but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection
# Based on the corrected code from Task 1,
#  further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"

entertainment_system = "projector" if venue == "large hall" else "audio system" and "conference room"
print(f'You will need a',venue,"with a", entertainment_system)

# Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes,
#  otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"


entertainment_system = "projector" if venue == "large hall" else "audio system" and "conference room"
print(f'You will need a',venue,"with a", entertainment_system)
catering_options = input("Do you eat vegeterian?(yes/no):")
if catering_options == "yes":
    print(f'We recommend Veggie Delight Caterers')
else:
    print(f'We recommend Gourmet Meal Caterers')





