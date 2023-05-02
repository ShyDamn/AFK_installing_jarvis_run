import re

# Открываем файлы для чтения и записи
with open('only_names.txt', 'r') as input_file, open('russian_names.txt', 'w') as output_file:

    # Список правил звучания для перевода с английского на русский
    rules = {
    # Буквосочетания
    'dg': 'дж',
    'xel': 'ксель',
    'illu': 'иллю',
    'dc': 'диси',
    'll': 'л',
    'ff': 'ф',
    'mm': 'м',
    'pp': 'п',
    'dc': 'диси',
    'mate': 'мэйт',
    'pho': 'фо',
    'sho': 'шо',
    'xe': 'ксэ',
    'xce': 'ксе',
    'aut': 'авт',
    'key': 'кей',
    'dow': 'доу',
    'spy': 'спай',
    'excel': 'эксель',
    'oo': 'у',
    'chr': 'хр',
    'micr': 'майкр',
    'dge': 'дж',
    'health': 'хелс',
    'check': 'чек',
    'pow': 'пав',
    'ech': 'ич',
    'and': 'энд',
    'tion': 'шн',
    'math': 'матс',
    'nel': 'нель',
    'note': 'ноут',
    'quick': 'квик',
    'ss': 'с',
    'mote': 'моут',
    'nn': 'н',
    'fax': 'факс',
    'player': 'плейер',
    'ices': 'исес',
    'mput': 'мпьют',
    'manage': 'мэнэдж',
    'cleanup': 'клинап',
    'view': 'вьюв',
    'iscsi': 'исцси',
    'odbc': 'одбси',
    'sourc': 'сурс',
    'drive': 'драйв',
    'pubg': 'пабг',
    'counter': 'контр',
    'strike': 'страйк',
    'secure': 'секьюр',
    'sche': 'ще',
    'fire': 'файр',
    'wall': 'вол',
    'care': 'кейр',
    'ware': 'вэйр',
    'dater': 'дэйтер',
    'speed': 'спид',
    'up': 'ап',
    'box': 'бокс',
    'shi': 'ши',
    'jarv': 'джарв',
    'lij': 'лидж',
    'idea': 'идея',
    'phpst': 'пиэйчпишт',
    'pych': 'пайч',
    'logi': 'лоджи',
    'tech': 'тек',
    'hub': 'хаб',
    'dd': 'д',
    'node': 'ноуд',
    'gef': 'джиф',
    'orce': 'орс',
    'expe': 'экспи',
    'rience': 'риэнс',
    'ance': 'анс',
    'open': 'оупен',
    'shee': 'щи',
    'iver': 'айвер',
    'shell': 'шел',
    'curi': 'кьюри',
    'python': 'питон',
    'ration': 'рэйшн',
    'cure': 'кьюр',
    'docs': 'докс',
    'speccy': 'спесси',
    'mation': 'мэйшн',
    'with': 'вис',
    'steam': 'стим',
    'power': 'павер',
    'wolf': 'вольф',
    'athem': 'атем',
    'base': 'бэйс',
    'pare': 'пэйр',
    'read': 'рид',
    'char': 'чар',
    'iobit': 'айобит',
    'line': 'лайн',
    'maxon': 'максон',
    'team': 'тим',
    'rend': 'рэнд',

    }

    # Проходимся по каждой строчке входного файла
    for name in input_file:

            # Удаляем пробелы и переносы строки
            name = name.strip()

            # Заменяем букву e в начале каждого слова на э
            words = name.split()
            words = [word.replace('e', 'э', 1) if word.startswith('e') else word for word in words]

            # Удаляем "e" в конце каждого слова
            words = [word.rstrip('e') for word in words]

            # Собираем строку обратно
            name = ' '.join(words)

            # Применяем правила звучания
            for pattern, replacement in rules.items():
                    if pattern[0] == 'e':
                            name = re.sub(rf'\b{pattern}\b', replacement[0] + name[len(pattern) - 1:], name)
                    else:
                            name = re.sub(pattern, replacement, name)

            # Создаем словарь с символами и их переводами
            translation_dict = str.maketrans('abcdefghijklmnopqrstuvwxyz',
            'абкдефгхижклмнопкрстуввхиз')

            # Применяем перевод к строке
            russian_name = name.translate(translation_dict)

            # Записываем результат в выходной файл
            output_file.write(russian_name + '\n')
