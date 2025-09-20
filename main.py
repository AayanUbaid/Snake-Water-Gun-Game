import random 

computer = random.choice([1, -1, 0])

your_choice = input("""   s for Snake   
   w for water
   g for gun
Enter your Choice: """)

you_dict = {
    's': 1,
    'w': -1,
    'g': 0
}

reversed_dict = {1: 'snake', -1: 'water', 0: 'gun'}

if your_choice not in you_dict:
    print("Invalid Input")
else:
    your_num = you_dict[your_choice]

    print(f"You choose {reversed_dict[your_num]} \nComputer choose {reversed_dict[computer]}")

    if computer == your_num:
        print("It's a draw!")
    else:
        if computer == 0 and your_num == 1:
            print("You Lose!")
        elif computer == 0 and your_num == -1:
            print("You Win!")
        elif computer == 1 and your_num == 0:
            print("You Win!")
        elif computer == 1 and your_num == -1:
            print("You Lose!")
        elif computer == -1 and your_num == 0:
            print("You Lose!")
        elif computer == -1 and your_num == 1:
            print("You Win!")
        else:
            print("Something Went Wrong ...")

            




