def spam(divideBy):
    try:
        return 42 / divideBy
    except:
        print('Error div by zero')
        return 0

print(spam(1))
print(spam(2))
print(spam(3))
print(spam(4))
print(spam(0))
