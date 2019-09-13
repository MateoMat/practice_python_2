# Write a program which asking user for a numer then print message depend on value
def play_game():
    user_input = input('Enter your age: ')
    if int(user_input) >= 18:
        print("In Poland you can drink alcohol")
    else:
        print("In Poland you cannot drink alcohol")

play_game()

repeat_question = input("Do you wanna play again ? type Y/N ")
while repeat_question.upper() == "Y" :
    play_game()    
else :
    print("O.k. Goodbye;-)")
