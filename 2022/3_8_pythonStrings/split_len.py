first_name = "Reiko"
last_name = "Matsuki"


def password_generator(first_name, last_name):
    firstLast3 = len(first_name) - 3
    lastLast3 = len(last_name) - 3
    solution = first_name[firstLast3:] + last_name[lastLast3:]
    return solution


combined = password_generator(first_name, last_name)

print(combined)
