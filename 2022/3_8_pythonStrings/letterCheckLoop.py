# letter checker using for loop


def letter_check(word, letter):
    for i in word:
        if (i == letter):
            return True
            break
    return False


check = letter_check('animal', 'l')
# print(check)

# letter checker using python shortcut


def contains(big_string, little_string):
    if little_string in big_string:
        return True
    return False


def common_letters(string_one, string_two):
    sharedLetters = []
    for i in string_one:
        if i in string_two and not (i in sharedLetters):
            sharedLetters.append(i)
    return sharedLetters


check1 = common_letters('animals', 'animal')


# password generator project

firstName = 'Abe'
lastName = 'Simpson'


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        firstChanged = first_name
    elif len(first_name) >= 3:
        firstChanged = first_name[:3]
    lastChanged = last_name[:4]
    username = firstChanged + lastChanged
    return username


def password_generator(username):
    lastChar = username[-1]
    noLastChar = username[0:-1]
    password = lastChar + noLastChar
    return password


username = username_generator(firstName, lastName)
password = password_generator(username)

# print(username)
print(password)
