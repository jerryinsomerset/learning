def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


print('Please enter a number')

myNumber = 0
while myNumber == 0:
    try:
        myNumber = int(input())
    except:
        print('No good')

while myNumber != 1:
    myNumber = collatz(myNumber)
    print(myNumber)
