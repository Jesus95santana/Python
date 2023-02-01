hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.
length = len(prices)
total = 0

for price in prices:
    total += price

average = total / length

print('Average Haircut Price: \n' + str(average))

#That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

new_prices = [price - 5 for price in prices]

print('Regular Prices: \n' + str(prices))
print('New Prices: \n' + str(new_prices))

# Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

#new_prices = [25, 20, 35, 15, 15, 30, 45, 30]
#last_week = [2, 3, 5, 8, 4, 4, 6, 2]

revenue = 0
time_rotation = 0
for prices in new_prices:
    revenue += prices * last_week[time_rotation]
    time_rotation += 1

print('Weekly revenue is: \n' + str(revenue))
print('Daily revenue is: \n' + str(revenue/7))

#Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

# hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
#new_prices = [25, 20, 35, 15, 15, 30, 45, 30]

cuts_under_30 = [hairstyles[i]
                 for i in range(len(hairstyles)) if new_prices[i] <= 30]

print(cuts_under_30)
