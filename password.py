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