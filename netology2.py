import re

"""Задание № 1"""


class Cookbook:
    def __init__(self, name):
        self.cook_book = None
        self.name = name

    def create(self, filepath):
        cook_book = {}
        with open(filepath, 'r', encoding='utf-8') as file:
            bludo = ''
            listingr = []
            ingrdict = {}
            for f in file:
                f = f.strip()
                if (not re.findall('[|]', f)
                        and not re.findall('[\d]', f) and f not in '\n'):
                    if bludo != f:
                        listingr = []
                        bludo = f
                    else:
                        bludo = f
                if re.findall('[|]', f):
                    arca = f.split(' | ')
                    ingrdict['ingredient_name'] = arca[0]
                    ingrdict['quantity'] = arca[1]
                    ingrdict['measure'] = arca[2]
                    listingr.append(ingrdict)
                    ingrdict = {}
                try:
                    cook_book[bludo] = listingr
                except:
                    continue
        self.cook_book = cook_book
        return print('Cookbook has been created')


cookbook1 = Cookbook('First')
cookbook1.create('recipes.txt')
print(cookbook1.cook_book)

"""Задание № 2"""


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for smth in cookbook1.cook_book.items():
        for dish in dishes:
            if dish == smth[0]:
                for i in smth[1]:
                    resultik = {list(i.items())[1][0]: int(list(i.items())[1][1]) * person_count,
                                list(i.items())[2][0]: list(i.items())[2][1]}
                    prom = i['ingredient_name']
                    stringes = ', '.join(list(result.keys()))
                    if prom in stringes:
                        result[prom]['quantity'] = result[prom]['quantity'] + resultik['quantity']
                    else:
                        result[prom] = resultik
    return print(result)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

""" Задание № 3"""


def createfile(filename):
    with (open('1.txt', 'r+', encoding='utf-8') as file1,
          open('2.txt', 'r+', encoding='utf-8') as file2,
          open('3.txt', 'r+', encoding='utf-8') as file3):
        dlina1 = len(file1.readlines())
        dlina2 = len(file2.readlines())
        dlina3 = len(file3.readlines())
        file1.seek(0)
        file2.seek(0)
        file3.seek(0)
        spisok = [(file1.name, dlina1, file1.readlines()),
                  (file2.name, dlina2, file2.readlines()),
                  (file3.name, dlina3, file3.readlines())]
        spisoksort = sorted(spisok, key=lambda x: x[1])
        with open(filename, 'w+', encoding='utf-8') as itogfile:
            for i in range(3):
                itogfile.write(spisoksort[i][0])
                itogfile.write('\n')
                itogfile.write(str(spisoksort[i][1]))
                itogfile.write('\n')
                itogfile.write(''.join(spisoksort[i][2]))
                if i != 2 and ''.join(spisoksort[i][2])[-1] != '\n':
                    itogfile.write('\n')
    return print(f'Файл {filename} успешно создан')


createfile('result.txt')
