import functions_book as fb
import functions_read_write_file as frw
import checking_file as cf

#Создание объекта Member и его методов#
class Member:

    #Словарь пользователя где ключи - имя поля а в значениях - значение этого поля
    def __init__(self, listfields, arg):
        self.data = dict(zip(listfields, arg))

    #Возвращение имени и фамилии одной строкой
    def identifier(self):
        return ' '.join([self.data['Имя'], self.data['Фамилия']]).lower()
    
    #Принимает ключ и новое значение. Изменяет значение по ключу
            #или создает новую запись если ключа еще нет
    def parametr(self, key, values):
        self.data[key] = values

    #Возвращает значение поля возраст
    def years(self):
        return self.data['возраст']
 
    #Возвращает множество значений словаря в нижнем регистре
    def show(self):
        return set(map(str.lower, list(self.data.values())))
 
    #Возвращает список ключей
    def change(self):
        return list(self.data.keys())
 
    #Возвращает строку значений
    def __str__(self):
        return ' '.join(list(self.data.values()))

