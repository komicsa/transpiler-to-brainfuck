symbols = input("Enter any characters:")

valid_symbols = "!@#$%^&*()_-+={}[]"

if symbols == '':
    print("None of characters have been entered. Please try again")
else:
    for ch in symbols:
        if symbols.isalnum() is True:
            print('No symbols have been detected in the input')
            break
        else:
            if ch not in valid_symbols:
                print('There are symbols mixed with other characters')
                break
    else:
        print('Your input contains symbols only')