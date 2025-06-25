print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1=input("select which side of the bank of the river u would choose either left or right\n").lower()
if choice1=='left':
    choice2=input("select u want to swim or wait\n").lower()
    if choice2=='wait':
        choice3=input("select door either the red or blue or yellow\n").lower()
        if choice3=='red':
            print("Burned by fire.Game Over.")
        elif choice3=='blue':
            print("Eaten by beasts.Game Over.")   
        elif choice3=='yellow':     
            print("you win")
        else:
            print("you are out of the game.")
    else:
        print("Attacked by trout.Game Over")
else:
    print("end the game.")   