## Часть чтения и записи в файл ##

import pickle # модуль для сохранения объектов в файл

def readfile(name):
    try:
        with open(name, 'rb') as f:
            return  pickle.load(f)
    except:
        print('\t\tДанных еще не сохранено!\n ')
        return []
        
def savedata(obj,name):
    file = open(name,'wb')
    pickle.dump(obj , file)