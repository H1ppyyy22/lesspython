#TODO Задание 1
def coordination(x, y):
    if x > 0 and y > 0:
        print('I')
    elif x < 0 and y > 0:
        print('II')
    elif x < 0 and y < 0:
        print('III')
    elif x > 0 and y < 0:
        print('IV')
    
print(coordination(11, -2))