user_plate = str(input('Please enter your plate'))

our_plate = 'AAA-111'

if '-' in user_plate:
    total_accurate_char = 0
    for i in user_plate:
        if i in our_plate:
            total_accurate_char += 1
    if total_accurate_char == 7:
        print('This is the correct plate number')
    elif total_accurate_char == 6:
        print('Only 6 characters match')
    elif total_accurate_char == 5:
        print('Only 5 characters match')
    elif total_accurate_char == 4:
        print('Only 4 characters match')
    elif total_accurate_char == 3:
        print('Only 3 characters match')
    elif total_accurate_char == 2:
        print('Only 2 characters match')
    elif total_accurate_char == 1:
        print('Only 1 characters match')
    else:
        print('Only - correct')
else:
    print('This plate is not from Colorado')
