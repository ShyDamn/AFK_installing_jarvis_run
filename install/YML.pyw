import os
import yaml

# Указываем путь для создания директории
directory_path = r'C:\jarvis-app\commands\run'

# Читаем данные из файлов
with open('russian_names.txt', 'r', encoding='windows-1251') as russian:
    russian_names = russian.read().splitlines()
with open('only_names.txt', 'r', encoding='windows-1251') as only:
    only_names = only.read().splitlines()

# Создаем директорию, если ее еще нет
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Создаем yml файлы
for russian_name, only_name in zip(russian_names, only_names):
    file_name = f"{only_name}.yml"
    file_path = os.path.join(directory_path, file_name)

    # Создаем словарь с данными для yml файла
    data = {
        'list': [
            {
                'command': {
                    'action': 'ahk',
                    'exe_path': f"ahk/{only_name}.exe",
                    'exe_args': f""
                },
                'voice': {
                    'sounds': ['ok1', 'ok2', 'ok3']
                },
                'phrases': [
                    f"запусти {russian_name}",
                    f"открой {russian_name}"
                ]
            }
        ]
    }

    # Записываем данные в yml файл
    with open(file_path, 'w', encoding='windows-1251') as yml_file:
        yaml.dump(data, yml_file, default_flow_style=False, allow_unicode=True)
