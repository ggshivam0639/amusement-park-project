# EG5-10 Ride Selector Start
print('''Welcome to our Theme Park
These are the available rides:
1. Scenic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator
''')                

ride_number_text = input('Please enter the ride number you want: ')
ride_number = int(ride_number_text)

while ride_number<1 or ride_number>5:
    print('There is no such ride.')
    while True:
        try:
            ride_number_text = input('Please enter the ride number you want: ')
            ride_number = int(ride_number_text)
            break                                             # data validation with break statement   # checking for the data validation of the ride number, it must be in digits rather than characters.
        except ValueError:
            print('Invalid number Text, please enter number in digits')
        except KeyboardInterrupt:
            print('Please do not try to stop the program')
print(f'You have selected ride number {ride_number}.')


if ride_number == 1:
    print('You have selected the Scenic River Cruise')
    print('There are no age limits for this ride')
else:                                                                   # We need to get the age of the user
    age_input_valid =False                                                #check age validation  #data validation with boolean variable
    while age_input_valid==False:
        try:
            age_text = input('Please enter your age: ')
            age = int(age_text)
            age_input_valid=True                                   # as the age data is valid input it will go for the next condition
        except ValueError:
            print('invalid number text.Please enter in digits')
    while age<1 or age>95:
                                                                                    #repeat this code as age is not valid
        print('Your entered age is not valid.')
        age_text = input('Please enter your age: ')
        age = int(age_text)
        print(f'Your entered age is {age}')

if ride_number == 2:
    print('You have selected the Carnival Carousel')
    if age >= 3 and age <= 70:
        print('You can go on the ride.')
    else:
        print('Sorry. you are too young or too old for this ride.')
if ride_number == 3:
    print('You have selected the Jungle Adventure Water Splash')
    if age >= 6 and age <= 70:
        print('You can go on the ride.')
    else:
        print('Sorry. You are too young or too old for this ride.')
if ride_number == 4:
    print('You have selected the Downhill Mountain Run')
    if age >= 8 and age <= 70:
        print('You can go on the ride.')
    else:
        print('Sorry. You are too young or too old for this ride.')
if ride_number ==5:
    print('You have selected The Regurgitator')
    if age<=12:
                                                                                      #yield you are not too young
        if age > 70:
                                                                              #you are too old
            print('Sorry. You are too old')
        else:
            print('Sorry. You are too young')
    else:
        print('You can go on the ride')
