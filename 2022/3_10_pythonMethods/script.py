from datetime import datetime
from decimal import Decimal
import random


def currentTime():
    current_time = datetime.now()
    print(current_time)


def randomNum():
    randomList = [
        random.randint(1, 100) for i in range(101)
    ]
    choice = random.choice(randomList)
    print(choice)


def decimalFunction():
    # Fix the floating point math below:
    two_decimal_points = Decimal('0.2') + Decimal('0.69')
    print(two_decimal_points)

    four_decimal_points = Decimal('0.53') * Decimal('0.65')
    print(four_decimal_points)
