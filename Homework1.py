def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    if n < 0:
        print(n)
        countup(n+1)
    else:
        print('Blastoff')

number = int(input('Please write the number: '))
if number >= 0:
    countdown(number)
else:
    countup(number)
