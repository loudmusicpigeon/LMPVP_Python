#  review the NUMBER GUESS code then run 
secret_word = "code"
guess_limit = 10

while True:
    number_guess = input("guess the secret word: ")
    if number_guess == secret_word:
        print("Yes", number_guess,"is correct!\n")
    else:
        while True:
            print(number_guess,"is incorrect\n")
            guess_count = 1
            att = guess_limit - 1
            print('attempts left:', att)