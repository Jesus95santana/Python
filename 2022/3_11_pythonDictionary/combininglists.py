# drinks = ["espresso", "chai", "decaf", "drip"]
# caffeine = [64, 40, 0, 120]
#
# zipped_drinks = {key: value for key, value in zip(drinks, caffeine)}
#
# print(zipped_drinks)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key: value for key, value in zip(songs, playcounts)}

plays['Purple Haze'] = 1
plays['Respect'] = 94

library = {'The Best Songs': plays, 'Sunday Feelings': {}}

print(plays)
print(library)
