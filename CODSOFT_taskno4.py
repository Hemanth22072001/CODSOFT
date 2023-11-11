import random

exit=False
user_points=0
computer_points=0

while exit==False:
    options=['rock','paper','scissor']
    print("\n---WELCOME TO ROCK_PAPER_SCISSORS GAME---")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    print("4.Get Scores")
    print("5.Exit")
    user_input=input("Choose your to number to play or to get score or to exit: ")
    computer_input=random.choice(options)

    if user_input=='5':
        print("\nThank You For Playing")
        print("\n-x-Game Ended-x-")
        exit=True
        print(f"Total AI Score: {computer_points}")
        print(f"Total User Score: {user_points}")

    if user_input=="1":
        if computer_input=="rock":
            print("Its a tie.")
            print(user_points)
            print(computer_points)
            print(f"AI's choice was: {computer_input}")
        elif computer_input=="scissor":
            print("User Won.")
            user_points+=1
            print(f"AI's choice was: {computer_input}")
            print(user_points)
            print(computer_points)
        elif computer_input=="paper":
            print("AI Won.")
            computer_points+=1
            print(f"AI's choice was: {computer_input}")
            print(user_points)
            print(computer_points)

    elif user_input=="2":
        if computer_input=="paper":
            print("Its a tie.")
            print(user_points)
            print(computer_points)
            print(f"AI's choice was: {computer_input}")
        elif computer_input=="rock":
            print("User Won.")
            user_points+=1
            print(f"AI's choice was: {computer_input}")
            print(user_points)
            print(computer_points)
        elif computer_input=="scissor":
            print("AI Won.")
            computer_points+=1
            print(f"AI's choice was: {computer_input}")
            print(user_points)
            print(computer_points)

    elif user_input=="3":
        if computer_input=="scissor":
            print("Its a tie.")
            print(user_points)
            print(computer_points)
            print(f"AI's choice was: {computer_input}")
        elif computer_input=="paper":
            print("User Won.")
            user_points+=1
            print(f"AI's choice was: {computer_input}")
            print(user_points)
            print(computer_points)
        elif computer_input=="rock":
            print("AI Won.")
            computer_points+=1
            print(f"AI's choice was: {computer_input}")
            print(user_points)
            print(computer_points)

    elif user_input=="4":
        print("\n--TOTAL SCORS ARE--")
        print(f"The User Gained Score is: {user_points}")
        print(f"The AI Gained Score is: {computer_points}")