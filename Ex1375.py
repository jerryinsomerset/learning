while True:
    print('Who are you?')
    name = input()
    if name != 'Jerry':
          continue
    print('Hello Jerry, what is the password?')
    print('hint it\'s a fish')
    passWord = input()
    if passWord == 'swordfishes':
          break

print('Access granted')


        
