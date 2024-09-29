import random
user_count=0
sys_count=0
option = ["stone","paper","scissor"]
while True:
    user_guess = input("Please choose Stone/paper/scissor or Q to quit: ").lower()
    if user_guess == "q":
        break

    if user_guess not in option:
        print("Please choose anyone mentioned in option")
        continue

    random_num =random.randint(0,2)
    # 0-stone, 1- paper,2-scissor

    comp_pick = option[random_num]
    # print(comp_pick)
    if user_guess =="stone" and comp_pick == "paper":
        print("I picked Paper")
        print("I Won :)")
        sys_count+=1
    elif user_guess=="paper" and comp_pick == "scissor":
        print("I picked Scissor")
        print("I Won :)")
        sys_count+=1
    elif user_guess=="scissor" and comp_pick=="stone":
        print("I picked Stone")
        print("I Won :)")
        sys_count+=1

    elif user_guess=="paper" and comp_pick == "stone":
        print("I picked Stone")
        print("You wins :( ")
        user_count+=1
    elif user_guess=="scissor" and comp_pick == "paper":
        print("I picked Paper")
        print("You Wins :( ")
        user_count+=1
    elif user_guess=="stone" and comp_pick=="scissor":
        print("I picked Scissor")
        print("You Wins :( ")
        user_count+=1

    elif user_guess=="paper" and comp_pick == "paper":
        print("I picked paper")
        print("We are same! Lets retry")
    elif user_guess=="scissor" and comp_pick == "scissor":
        print("I picked Scissor")
        print("We are same! Lets retry")
    else:
        print("I picked Stone")
        print("We are same! Lets retry")

print("Happy to play with you :)")
if sys_count>user_count:
    print(f"Hurry! I Win the match. Your score is {user_count} and my score is {sys_count}")
else:
    print(f"Oops! You Wins the match. My score is {sys_count} and your score is {user_count}")

print("Goodbye! Have a nice day")


