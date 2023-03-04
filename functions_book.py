## Функции для работы со справочником ##

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
    def parameter(self, key, values):
        self.data[key] = values

    #Возвращает значение поля возраст
    def years(self):
        return self.data['Возраст']
 
    #Возвращает множество значений словаря в нижнем регистре
    def show(self):
        return set(map(str.lower, list(self.data.values())))
 
    #Возвращает список ключей
    def change(self):
        return list(self.data.keys())
 
    #Возвращает строку значений
    def __str__(self):
        return ' '.join(list(self.data.values()))
    


#Просмотр всех записей справочника    
def look(data):
    for obj in data:
        print(obj)
 
#Поиск по справочнику
def search(data,line):
    trigger = 1 
    for obj in data:
        if line.issubset(obj.show() ):
            trigger = 0
            print(f'\t Результат - {obj}')
    if trigger:
        print('Совпадений не найдено')
 
def search_age(data,member):
    for obj in data:
        if obj.identifier().lower() == member.lower():
            print( obj.years())
            return
   
#Добавление новой записи
def addmember(listfields, data, name):
    database = cf.data_input(listfields)
    client = ' '.join(database[:2])
    for obj in data:
        client == obj.identifier()
        print('Имя и фамилия существуют! Выберите другие!')
        return
                      
    memb = Member(listfields, database) # создаем обьект экземпляр класса
    print( 'Пользователь добавлен')
    data.append(memb) # добавляем обьект в список
    frw.savedata(data,name) # перезаписываем файл c новыми данными
    
#Удаление по имени и фамилии 
def del_memb(data):
    member = ' '.join(map(str.lower, [input('Имя > '), input('Фамилия > ')]))
    for i,obj in enumerate(data):
        if obj.identifier() == member:
            data.pop(i)
            frw.savedata(data,frw.name) # перезаписываем файл c новыми данными
            print('Удалено')
            return

#Изменение значения по полю или добавление если еще нет
def change(data, member):
    for obj in data: 
        if  obj.identifier() == member:
            key = input('Введите имя поля > ')
            if key not in obj.change():
                print('Нет такого поля!')
                if input(' Создать поле? д\н > ').lower() == 'д':
                    key = input('Введите имя поля > ')
                else:
                    return
            values = input('Введите значение > ')
            obj.parameter(key, values)
            break