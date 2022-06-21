import random


while True:
    game = 'start'
    game = input("enter start to begin ")
    if game == 'start'  :
        print('welcome')

        while True:
            choices = ["R","P","S"]

            computer = random.choice(choices)
            player = None

            while player not in choices:
                player = input("R, P, or S?: ").lower()

                #if its a tie among players
                if player == computer:
                    print("computer: ",computer)
                    print("player: ",player)
                    print("Tie!")

                    continue

                elif player == "R":
                    if computer == "P":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You lose!")

                    elif computer == "S":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You win!")

                

                elif player == "S":
                    if computer == "R":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You lose!")

                    elif computer == "P":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You win!")
            
        

                elif player == "P":
                    if computer == "S":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You lose!")

                    elif computer == "R":
                        print("computer: ", computer)
                        print("player: ", player)
                        print("You win!")

                elif player != choices:
                    print("wrong choice")
                    continue
        
            #to check if the player wants to play again.
            replay = input("Would you like to play again? (yes/no): ").lower()

            if replay != "yes":
                break
            print("Bye!")

    else:
        print("goodbye see ya")
    break
