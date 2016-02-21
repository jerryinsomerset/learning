count = 1 

while True:
    print('Please enter your name')
    name = input()
    if count < 3:
        count = count +1
        print('and again')
        continue
    elif name == 'Jerry':
        break

print('Thank you')


    
