# returns a string
def trip_planner(name):
    print('hello ' + str(name) + ' its time to go to vacation')


trip_planner('michael')

# adds all numbers and get median of them
numbers = [2, 3, 6, 1, 9, 5]


def averageMath(nums):
    total = 0
    for num in nums:
        total += num
    average = total / len(nums)
    print(str(average))


averageMath(numbers)
