#@Dev_Aladinh production
#calculator app


def status():
    a = "add"
    b = "substract"
    c = "multiply"
    d = "divide"
    
    print("\nWhich operation do you wannah do.> a:{add}, b:{substract}, c:{multiply}, d:{divide}")

    operation = input(":) ").lower()

    if operation == "a":
        operation = addition()

    elif operation == "b":
        operation = subtraction()

    elif operation == "d":
        operation = division()

    elif operation == "c":
        operation = multiplication()

    else:
        print("\n-->The operation couldn't be found<--")

    print("Enter the two numbers you wannah use: ")


def addition():
    number_a = int(input("Num 1:  "))
    number_b = int(input("Num 2:  "))
   
    Answer = number_a + number_b
    print("The answer is-->" + str(Answer))

def subtraction():
    number_a = int(input("Num 1:  "))
    number_b = int(input("Num 2:  "))

    Answer = number_a - number_b
    print("The answer is-->" + str(Answer))

def division():
    number_a = int(input("Num 1:  "))
    number_b = int(input("Num 2:  "))

    Answer = number_a / number_b
    print("The answer is-->" + str(Answer))


def multiplication():
    number_a = int(input("Num 1:  "))
    number_b = int(input("Num 2:  "))

    Answer = number_a * number_b
    print("The answer is-->" + str(Answer))


def calculator():
    print("\nHelloh user ^!^!^\nEnter your name.")
    identity = input(":) ").lower()

    print("\nWelcome " + identity + " to my simple calculator app\nNOTE:YOU CAN ONLY INPUT TWO NUMBERS\n\nDo you wannah play?{yes / no}")
    play= input(":) ").lower()

    if play in ["yes", "yeap", "yeap", "ok", "okay"]:
        play = status()
    else:
        print("\nIt was a nice time with you, welcome again next time^:^")
        quit()

calculator()


def next_play():
    print("\nDo you wannah play again? {yes or no}")
    play_again = input(":) ").lower()

    if play_again == "yes":
        play_again = status()
    
    else:
        print("Welcome " + identity + " next time to the play ^.^")

next_play()
        



