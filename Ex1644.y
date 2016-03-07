import random

def getCube(operand_1, operand2, operand3):
    return operand_1 * operand2 * operand3


myInt1 = random.randint(1,9)
myInt2 = random.randint(1,9)
myInt3 = random.randint(1,9)

myCube = getCube(myInt1,myInt2,myInt3)
print(str(myInt1) + ' * ' + str(myInt2) + ' * ' + str(myInt3) + ' = ' + str(myCube))

