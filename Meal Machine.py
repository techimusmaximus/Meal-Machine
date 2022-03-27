# the following script randomly generates either a main dish, a side dish, or both for the indecisive consumer
# secrets will allow me to roll randomly later on
import secrets
print("Welcome to the Food Machine! This script will help you figure out what to eat.")

# the _dish series has either main or side dishes. titular
main_dish = ["chicken and dumplings", "salmon", "steak", "cheeseburger", "hamburger", "soup", "breakfast burrito",
             "fried chicken", "tuna", "fried oysters", "crab legs", "sweet and sour chicken", "pizza", "lobster tail",
             "calamari", "shrimp kabobs", "beef skewers", "beef stew", "kielbasa with sauerkraut", "meatloaf"]

side_dish = ["french fries", "mashed potatoes", "grilled asparagus", "fried rice", "hash browns", "grits", "cole slaw",
             "sausage patties", "breadsticks", "mozzarella sticks", "cheese curds", "white rice", "bacon slices",
             "corn on the cob", "Brussels sprouts", "roasted broccoli", "biscuits", "side salad", "baked beans"]

# the answer_pool series allows for user input to quit the script (with a mean exit message) or continue
answer_pool_affirm1 = ("Yes", "Yeah", "yes", "yeah", "y", "Y", "sure", "Sure", "hungry", "Hungry", "me hungry")
answer_pool_deny1 = ("No", "no", "nah", "Nah", "never", "Never", "Me no hungry", "me no hungry", "I am full", "i full")

# user assigns answer1 a value here
answer1 = input("Are you hungry? ")

# before user interest or disinterest is solidified, it makes sense to allow a while-loop in case of a typo
while answer1 not in answer_pool_affirm1 and answer1 not in answer_pool_deny1:
    print("Sorry, your answer was unclear.")
    answer1 = input("Are you hungry? ")

# quit outcome. quits script + snarky exit message
if answer1 in answer_pool_deny1:
    print("Then what are you doing here?")
    quit()
# affirm outcome. script continues
elif answer1 in answer_pool_affirm1:
    print("Copy that.")

# user now decides interest in main dishes, side dishes, or both
# having multiple lists seems unwieldy, but I couldn't get indexing to work for the life of me. need more experience
answer_pool_main_dish = ["main dish", "Main dish", "main", "Main"]
answer_pool_side_dish = ["side dish", "Side dish", "side", "Side"]
answer_pool_side_and_dish = ["Side and main", "side and main", "both", "Both", "Let's do both", "let's do both"]

# simple stuff. asks the user which of the three outcomes they want
answer2 = input("Would you like a main dish, side dish, or both? ")

# typo-checker loop. just like the while-loop for answer1
while answer2 not in (answer_pool_main_dish + answer_pool_side_dish + answer_pool_side_and_dish):
    print("Sorry, your answer was unclear.")
    answer2 = input("Would you like a main dish, side dish, or both? ")

# the "secrets" import comes into play now
# outcome where user requests a main dish
if answer2 in answer_pool_main_dish:
    print("Just a main dish. Gotcha!")
    print("I recommend an entree of " + str(secrets.choice(main_dish)) + ".")
# outcome where user requests a main dish
elif answer2 in answer_pool_side_dish:
    print("Just a side dish. Gotcha!")
    print("I recommend a side of " + str(secrets.choice(side_dish)) + ".")
# outcome where the user requests a main and side dish
else:
    print("A main dish and a side dish. Coming right up!")
    print("I recommend an entree of " + str(secrets.choice(main_dish)) +
          " with a side of " + str(secrets.choice(side_dish)) + ".")

# exit message
print("Thank you for using the Food Machine!")
