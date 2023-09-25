from My_Hut import My_Hut
from Item import Item

# Display a welcome screen for the user
def welcomescreen():
    # Welcome screen
    print("Welcome to The_Deep! Don't drown, survive and explore to live!")
    print("Make sure to always look around and watch your back before taking your next step!")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print()
    print("You just woke up and something isn't just right.")
    print()


# Display the menu for the user.
def displaymenu():
    print("What do you want to do?")
    print("1. Take your time to get dressed nicely, before....")
    print("2. Put on something quick and storm out, before....")
    print("3. I'm comfortable as is and will leave, before....")
    print("4. You know exactly what's going on and plan your adventure ahead of you")
    print("5. Hesitating, you need some time to look around")
    print("0. Turn around and go back to sleep, this is just a nightmare")


# Ask user for input
def fetchinput():
    ans = input("Please enter your choice: ")
    if ans.isdigit():                          # True if ans is a number, False if it is something else
        if 0 <= int(ans) < 4:                  # Check if the input is between 0 and 3
            return int(ans)
    return -1                                  # Will return -1 if the other conditions are false.


###
# Define environment

kayak = Item("Kayak", "This kayak can be inflated and used for 2 individuals")
scubatank = Item("This mouthpiece scubatank can be used for 10 minutes")
goggles = Item("You'll need this to be able to see underwater")
fins = Item("To be attached to your feet for faster swimming")
wetsuit = Item("A full-body suit made of rubber to protect from the colder water in the deep")
bathingsuit = Item("A piece of clothing to protect your private parts from the elements")
paddle = Item("A long pole with broad blades on both ends used to move through the water")
bag = Item("A large and lightweight container to collect and carry your items")

# Define your Hut
hut = My_Hut("Hut")
hut.setdescription("The hut is illuminated by the two small windows opposite of each other and the round opening in the high ceiling. There seems to be an opening in the middle that looks like a small split in the wall")
hut.addopening("The split in the wall")

outside = My_Hut("Dock")
outside.setdescription("A structure lining up vessels")

#################################
#Main program

world = [hut]

welcomescreen()

#Main loop/Gameloop
run = True
while run:
    #Display the hut you are in.
    print(world.tostring())
