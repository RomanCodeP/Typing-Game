#### Game, You have to type the sentence
import time
import random
print("--------------------------")
print("Welcome to the Type test")
print("You will have to type exactly the sentence that is going to show up")

def intro():
    start = input("Type 'yes' to start: ")
    if start == "yes" or "Yes":
        game()

    else:
        print("------------------------")
        print("you have to type 'yes'")
        time.sleep(1)
        intro()

def game():
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(0.2)
    print("--------------")
    print(" ")
    Numberonetype = "Learning Python every day helps you improve your problem solving skills."
    Numbertwotype = "Programming can be challenging but practice makes everything easier."
    Numberthreetype = "The weather is beautiful today" 
    RandomNumber = random.randint(1, 3)
    print("debug:", RandomNumber)
    words = 0
    if RandomNumber == 1:
        typechallenge = Numberonetype
        words = 11
    elif RandomNumber == 2:
        typechallenge = Numbertwotype
        words = 9
    elif RandomNumber == 3:
        typechallenge = Numberthreetype
        words = 5
    firsttime = time.perf_counter()
    print(typechallenge)
    answer = input("------- Type: ")
    secondtime = time.perf_counter()
    if answer == typechallenge:
        timeSolve = secondtime - firsttime
        print("correct")
        print("You typed the sentence in:", timeSolve, "seconds")
        print("That's:", words / timeSolve, "Words per second")
        print("And: ", (words / timeSolve) * 60, "Words per minute")

    else:
        print("incorrect")
        time.sleep(1)
        game()
    


intro()
