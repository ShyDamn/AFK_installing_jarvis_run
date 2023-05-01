# Открываем файлы для чтения и записи
with open('only_names.txt', 'r') as input_file, open('russian_names.txt', 'w') as output_file:

    # Проходимся по каждой строчке входного файла
    for name in input_file:

        # Удаляем пробелы и переносы строки
        name = name.strip()

        # Создаем словарь с символами и их переводами
        translation_dict = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                         'абцдефгхижклмнопкрстуввхизАБЦДЕФГХИЙКЛМНОПКРСТУВВХИЗ')

        # Применяем перевод к строке
        russian_name = name.translate(translation_dict)

        # Записываем результат в выходной файл
        output_file.write(russian_name + '\n')
