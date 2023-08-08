# import logo from art.py
import art
# import dictionary from game_data.py
from game_data import data
# import random module, using randint to choose data dictionary
import random
# print logo
from replit import clear

# create a compare function to compare the second which is follower numbers parameter
def compare(first_item_chosen, next_item_chosen):
    first_followers = first_item_chosen['follower_count']
    next_followers = next_item_chosen['follower_count']
    print(first_item_chosen)
    print(first_followers)
    print(next_item_chosen)
    print(next_followers)
    if first_followers > next_followers:
        return True
    else:
        return False
# show two lines of data retrieved from game_data.py data dictionary
# random generate two items from data to compare

# print the vs logo between two lines
# get input of ("who has more followers? Type 'A' or 'B' ")
game_continue = True
first_item = random.randint(0,49)
first_item_chosen = data[first_item]
score = 0
print(art.logo)
while game_continue:
    print(f"Compare A: {first_item_chosen['name']}, a {first_item_chosen['description']}, from {first_item_chosen['country']}.")
    print(art.vs)
    next_item = random.randint(0,49)
    next_item_chosen = data[next_item]
    print(f"Against B: {next_item_chosen['name']}, a {next_item_chosen['description']}, from {next_item_chosen['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a":
        result = compare(first_item_chosen, next_item_chosen)
        clear()
        print(art.logo)
        if result == True:
            score += 1
            first_item_chosen = next_item_chosen
            print(f"You're RIGHT! Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
    elif answer == "b" :
        result = compare(first_item_chosen, next_item_chosen)
        clear()
        print(art.logo)
        if result == False:
            score += 1
            first_item_chosen = next_item_chosen
            print(f"You're RIGHT! Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
    else:
        print("invalid input")
        game_continue = False



# add a while loop for game continue



        
