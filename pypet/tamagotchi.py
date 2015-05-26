#variable and random number generator library needed for the guessing game
from random import randint
secret = randint(1,10)

#Variable needed to skip the beginning when finished
beginning_finished = False

#The pet's stats
pet_name = "Fluffy"
pet_photo = "<`)))><"
pet_status = "youngling"
pet_health = 5
pet_age = 5
pet_hunger = 5
pet_happiness = 5

#age based max values
max_health = 5
max_hunger = 5
max_happiness = 10

#Pictures and symboles used ingame
cat = "(=^o.o^=)__"
mouse = "<:3 )~~~~"
fish = "<`)))><"
owl = "(^0M0^)"

#A function to nicely print out the pets stats
def pet_stats():
    print(pet_name)
    print(pet_photo)
    print("Status: " + pet_status)
    print("Age: " + str(pet_age))
    print("Health: "  + pet_health * "♥")
    print("Hunger: " + pet_hunger * "*")
    print("Happines: " + pet_happiness * "☺")

#A function which checks if the pet is still alive
def is_alive():
    if pet_health > 0:
        return True
    else: 
        return False
        
#A function which let's the player choose his pet.
def  beginning():
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

def aging():
    global pet_status
    global max_health
    global max_happiness
    global max_hunger
    if pet_age == 5:
        pet_status = "adult"
        max_health = 10
        max_happiness = 8
        max_hunger = 7
        print("Congratulation your pet has become an adult. It needs less food now")
        print("and it's health has improved however it's grumpier than a youngling.")
    elif pet_age == 15:
        pet_status = "elderly"
        max_health = 7
        max_happiness = 5
        max_hunger = 10
        print("Congratulation your pet has become an elderly it needs now less food.")
        print("However it's health is worse and it's grumpier than an adult.")
        
#Increases the pets hungriness by +1 unless the hunger is bigger than
#the pet's maximum hunger. In this case the pet womits and looses hunger
#and health.
def feading():
    global pet_hunger
    print("Hungriness of " + pet_name + ": " + pet_hunger * "*")
    feading_confirmed = input("Do you want to feed your pet?")
    if feading_confirmed in ("Y","y"):
        pet_hunger = pet_hunger + 1

#A simple guessing game which increases the pet's happiness
def playing():
    global pet_happiness
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

#Beginning of the main routine which makes up the actual game.
#Only starts if the pet is still alive.
while is_alive():         
    if beginning_finished == False:
        #Let the player choose his pet and skip the beginning from then on.
        beginning()
        beginning_finished = True
        print()
        print()
        print("Your pet is currently a youngling which means it's needs a lot of attention.")
        print("Take good care of it or it will die very soon.")
    #Each round print the pets stats so that the player can see them.
    aging()
    print()
    pet_stats()
    print()
    #Present the player with activities to choose from
    print("What would you like to do?")
    print("1: Feading, 2: Playing")
    #Start the chosen activity and go back to the activity selector.
    chosen_activity = int(input("Choose the decired activity:"))
    if chosen_activity == 1:
        feading()
    elif chosen_activity == 2:
        playing()
print("Your pet died.")    
