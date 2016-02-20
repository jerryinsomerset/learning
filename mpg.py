# miles per gallon calculator 
litresPerGallon = 4.54609

print('MPG calculator')
print('==============')
print('Input mileage')
mileage = input()
print('Input litres used ')
litresUsed = input()
mpg = int(mileage) / (int(litresUsed) / litresPerGallon)
print('MPG = ' + str(mpg))

