toppings = ['pepperoni', 'pinnaple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)


print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

#new 2d list
pizza_and_prices = [
    [2, 'pepperoni'], [6, 'pinnaple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']
]

pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

print(pizza_and_prices)
print('The cheapest pizza is ' + str(cheapest_pizza))
print('The most expensive pizza is ' + str(priciest_pizza))

pizza_and_prices.pop()
print(pizza_and_prices)

pizza_and_prices.insert(1, [2.5, 'peppers'])
three_cheapest = pizza_and_prices[:3]

print(pizza_and_prices)
print(three_cheapest)
