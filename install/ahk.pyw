import os
import subprocess

folder_to_find = 'jarvis'  # Искомая папка
subfolder_to_find = 'commands'  # Искомая подпапка
subsubfolder_to_find = 'run'  # Искомая подпапка
new_folder = 'ahk'  # Новая папка для создания

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
                        for subsubroots, subsubdirs, subsubfiles in os.walk(os.path.join(subfolder_path)):
                            if subsubfolder_to_find in subsubdirs:
                                subsubfolder_path = os.path.join(subsubroots, subsubfolder_to_find)
                                directory_path = os.path.join(subsubfolder_path, new_folder)
                                os.makedirs(directory_path, exist_ok=True)

# Создать директорию, если она не существует
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Читать файл all_directory.txt и заполнять файлы .ahk
with open("all_directory.txt", "r") as file, open("only_names.txt", "r") as names_file:
    # Создать файл .ahk для каждой строки в файле all_directory.txt и каждого имени в файле only_names.txt
    for i, (line, name) in enumerate(zip(file, names_file)):
        # Создать путь к файлу .ahk внутри директории
        file_path = os.path.join(directory_path, f"{name.strip()}.ahk")
        
        # Открыть файл .ahk и записать текст с использование строки из файла all_directory.txt
        with open(file_path, "w") as ahk_file:
            ahk_file.write(f"run {line.strip()}")

# Получение списка .ahk файлов
ahk_files = [f for f in os.listdir(directory_path) if f.endswith('.ahk')]

# Компиляция .ahk файлов с помощью AutoHotkey
for ahk_file in ahk_files:
    input_file_path = os.path.join(directory_path, ahk_file)
    output_file_path = os.path.splitext(input_file_path)[0] + '.exe'
    subprocess.run(['C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe', '/in', input_file_path, '/out', output_file_path])

