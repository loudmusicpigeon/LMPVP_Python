#  review the NUMBER GUESS code then run 
guess = ''
secret_word = "code"
guess_limit = 10
guess_count = 0
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if (guess_count < guess_limit):
        guess = input('Guess the secret word: ')
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print('Out of guesses. Secret Word is "code"')
else:
    print('Correct Guess!!!')