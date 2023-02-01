user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

#Showing all keys in dictionary
users = user_ids.keys()

lessons = num_exercises.keys()

print(users)
print(lessons)

for names in user_ids:
    print(names)

# Adding all numbers in dictionary
total = 0

for num in user_ids.values():
    total += num
print(total)

# Getting BOTH
for datboi, datnum in user_ids.items():
    print('that boi is ' + datboi + '... that num is ' + str(datnum))
