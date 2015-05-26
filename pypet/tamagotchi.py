#variable and random number generator library needed for the guessing game
from random import randint
secret = randint(1,10)

#Global Variables
beginning_finished = False

#The pet's stats
pet_name = "Fluffy"
pet_photo = "<`)))><"
pet_status = "youngling"
pet_health = 5
pet_age = 1
pet_hunger = 5
pet_happiness = 5

#Pictures and symboles used ingame
cat = "(=^o.o^=)__"
mouse = "<:3 )~~~~"
fish = "<`)))><"
owl = "(^0M0^)"

def pet_stats():
    print(pet_name)
    print(pet_photo)
    print("Status: " + pet_status)
    print("Age: " + str(pet_age))
    print("Health: "  + pet_health * "♥")
    print("Hunger: " + pet_hunger * "*")
    print("Happines: " + pet_happiness * "☺")

def is_alive():
    if pet_health > 0:
        return True
    else: 
        return False
    
def  beginning():
    #Let's the player choose it's pet
    print("Which pet do you want to look after?")
    print("1: Cat, 2: Mouse, 3: Fish, 4: Owl")
    chosen_pet = int(input("Choose your pet:"))
    if chosen_pet == 1:
        pet_photo = cat
    elif chosen_pet == 2:
        pet_photo = mouse
    elif chosen_pet == 3:
        pet_photo = fish
    elif chosen_pet == 4:
        pet_photo = owl

def feading():
    global pet_hunger
    #Increases the pets hungriness by +1
    print("Hungriness of " + pet_name + ": " + pet_hunger * "*")
    feading_confirmed = input("Do you want to feed your pet?")
    if feading_confirmed in ("Y","y"):
        pet_hunger = pet_hunger + 1

def playing():
    global pet_happiness
    #A simple guessing game which increases the pet's happiness
    guess = 0
    while guess != secret:
        g = input("Guess the Number")
        guess = int(g)
        if guess == secret:
            print("You win!")
        else:
            if guess > secret:
                print("Your guess is too high")
            else:
                print("Too low")
    pet_happiness = pet_happiness + 1
    print("Game over!")

#Main routine
while is_alive():         
    if beginning_finished == False:
        beginning()
        beginning_finished = True
    print()
    pet_stats()
    print()
    print("What would you like to do?")
    print("1: Feading, 2: Playing")
    chosen_activity = int(input("Choose the decired activity:"))
    if chosen_activity == 1:
        feading()
    elif chosen_activity == 2:
        playing()
print("Your pet died.")    
