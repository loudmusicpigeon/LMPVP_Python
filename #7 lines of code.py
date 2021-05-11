#7 lines of code
import random
wt = int(input('Enter a number: '))
mult = random.randint(1,2500)
def multii(x,y):
    result = x*y
    return result
print(wt, '×', mult, '=', multii(wt,mult))