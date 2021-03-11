# create a variable named city to store input, add a prompt for the name of a city: print "the city name is " followed by the value stored in city
# get user input for a city name in the variable named city
city = input("Enter city name: ")
# print the city name
print("The city name is ", city)

# create variables to store input: name, age, get_mail
name = input("Enter your name: ")
age = input("Enter your age: ")
get_mail = input("Get mail? (y/n): ")
# create prompts for name, age and yes/no to being on an email list
# print description + input values
print('Name: ', name)
print('Age: ', age)
if get_mail == 'y':
    print('Wants email = yes')
else:
    print('Wants email = no')