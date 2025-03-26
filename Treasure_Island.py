print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction= input('You are at a crossroad. where do u want to go? '
                 'Type "left" or  "right" :\n').lower()

if direction== "left" :
    x=input('You have come to a lake . '
            'There is an island in the middle of the lake.'
            ' Type "Wait" to wait for boat. '
            'Type "swim" to swim across\n   ') .lower()
    if x == "wait":
        y=input('You arrive at the island unharmed. '
                'There is a house with 3 doors.One red, one yellow and one blue .'
                'Which colour do u choose? \n') .lower()
        if y=="red":
            print("Burned by fire . Game Over !")
        elif y== "yellow":
            print("You Win!!! congrats")
        elif y == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over!!")
    else:
        print("Attacked by  angry trout. Game over!")

else:
    print('Fall into a hole. Game Over!')
