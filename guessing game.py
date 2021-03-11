#  review the NUMBER GUESS code then run 
secret_number = "13"

while True:
    number_guess = input("guess the number 1 to 20: ")
    if number_guess == secret_number:
        print("Yes", number_guess,"is correct!\n")
        break
    else:
        print(number_guess,"is incorrect\n")
        if number_guess > secret_number:
            print('Your number is larger than the secret number')
        elif number_guess < secret_number:
            print('Your number is smaller than the secret number')