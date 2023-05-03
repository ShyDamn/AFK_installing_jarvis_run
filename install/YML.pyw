import os
import yaml

folder_to_find = 'jarvis-app'  # Искомая папка
subfolder_to_find = 'commands'  # Искомая подпапка
new_folder = 'run'  # Новая папка для создания

directory_path = None

for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    disk_to_search = f"{drive}:\\"
    if os.path.exists(disk_to_search):
        for roots, dirs, files in os.walk(os.path.join(disk_to_search, "\\")):
            # Если папка найдена, ищем в ней подпапку
            if folder_to_find in dirs:
                folder_path = os.path.join(roots, folder_to_find)
                for subroots, subdirs, subfiles in os.walk(os.path.join(folder_path)):
                    if subfolder_to_find in subdirs:
                        subfolder_path = os.path.join(subroots, subfolder_to_find)
                        directory_path = os.path.join(subfolder_path, new_folder)
                        os.makedirs(directory_path, exist_ok=True)

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
