# a program that generates a random event based on number
import random

statement1 = 'Yes - definitely'
statement2 = 'It is decidedly so'
statement3 = 'Without a doubt'
statement4 = 'Reply hazy, try again'
statement5 = 'Ask again later'
statement6 = 'Better not tell you now'
statement7 = 'My sources say no'
statement8 = 'Outlook not so good'
statement9 = 'Very Doubtful'

name = input('What is your name?\n')
question = input('Hello ' + name + ', ask me anything youd like and i will predict its outcome to you.\n')

statement_generator = random.randint(1, 9)

if statement_generator == 1:
    print(statement1)
elif statement_generator == 2:
    print(statement2)
elif statement_generator == 3:
    print(statement3)
elif statement_generator == 4:
    print(statement4)
elif statement_generator == 5:
    print(statement5)
elif statement_generator == 6:
    print(statement6)
elif statement_generator == 7:
    print(statement7)
elif statement_generator == 8:
    print(statement8)
elif statement_generator == 9:
    print(statement9)
