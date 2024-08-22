def check(password):
    score = 5
    
    if len(password) < 12:
        score = score - 1
        print('Your password should have a length of 12 characters or more.')

    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)

    if not (upper and lower):
        score = score - 1
        print('Your password should contain at least one upper case and one lower case letter.')

    number = any(char.isdigit() for char in password)
    if number != True:
        score = score - 1
        print('Your password should contain at least one number.')

    symbol = any(not char.isalnum() for char in password)
    if symbol != True:
        score = score - 1
        print('Your password should contain at least one symbol.')
        
    return str(score)

password = input('Password to be checked: ')
print('Your password gets a rating of ' + check(password) + '/5 stars')