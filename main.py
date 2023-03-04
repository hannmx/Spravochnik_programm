## Основная часть ##

import functions_book as fb
import functions_read_write_file as frw

name = 'data.pickle' # имя файла данных
data = frw.readfile(name) # при запуске читаем данные из файла получаем список экземпляров класса
listfields = ['имя','фамилия','номер','возраст','город'] # поля ключей и подсказок ввода
 
while True:
    
    print('''\n\t\tКоманды для работы со справочником:
    \t\tПросмотр всех записей справочника - 1
    \t\tПоиск по справочнику - 2
    \t\tДобавление новой записи - 3
    \t\t Удаление записи из справочника по Имени и Фамилии - 4
    \t\tИзменение любого поля в определенной записи справочника - 5 
    \t\tВывод возраста человека (записи) по Имени и Фамилии - 6
     \t\tВыход - 0 \n''')
    
    command = input('Команда: > ')
    
    if command == '1':
        fb.look(data)
    elif command == '2':
        line = set(input('что искать> ').lower().split())#любая подстрока (имя, имя фамилия, фамилия, номер)
        fb.search(data,line)
    elif command == '3':
        print('Введите данные или * при их отсутствии')
        fb.addmember(listfields, data, name)
    elif command == '4':
        fb.del_memb(data)
    elif command == '5':
        member = input('имя фамилия > ').lower()
        fb.change(data, member)
    elif command == '6':
        member = input('имя фамилия > ').lower()
        fb.search_age(data,member)
        
    elif command == '0':
        frw.savedata(data,name)
        print("Работа завершена") 
        raise SystemExit

