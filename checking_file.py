## Часть ввода и проверки данных ##

#Проверка на ввод только букв
def correct_input(text):
    name = input(f'{text} > ')
    if name == '*':
        return name 
    while not name.isalpha():
        print('не корректный ввод')
        name = input(f'{text} > ')
    return name.capitalize()
    
#Проверка номера 
def correct_number(text):
    print('Номер +7 код номер без пробелов -> ')
    number = input(f'{text} > ')
    while True:
        if number[0] == '+' and number[1:].isdigit() and len(number) == 12:
            return number
        print('Не корректно введены данные!')
        number = input(f'{text} > ')

#Проверка возраста        
def correct_age(text):
    age = input(f'{text} > ')
    while True:
        if age.isdigit() or age == '*':
            return age
        print('Введите возраст цифрами!')
        age = input(f'{text} > ')
    
#Функция получения данных
def data_input(listfields):
    list_fun = [correct_input, correct_input, correct_number, correct_age, correct_input]
    return [fun(text) for text, fun in zip(listfields, list_fun)]