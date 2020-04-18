### your task:
# input: 1  2    -> output: addition is  3
# input: 5  3    -> output: result is  0
# input: 11 1    -> output: subtraction is  10

first = input('Enter the first number ')
second = input('Enter the second number ')

if (second > first):
    print('addition is ', first + second)
else:
    # as you see we can write many if statements, one inside another
    if (second < 10):
        print('subtraction is ', second - first)
    else:
        print('result is ', 0)
