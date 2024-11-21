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

#TODO Задание 2
def ask_password():
    password = 'password'
    count = 0
    while count != 3:
        user_pass = input('Введите пароль: ')
        if user_pass != password:
            print('Неверный пароль!')
            count += 1
        elif user_pass == password:
            print('Пароль принят!')
            break

ask_password()