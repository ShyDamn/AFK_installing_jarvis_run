import os

# Путь к директории, в которой будут созданы файлы .ahk
directory_path = r"C:\jarvis-app\commands\run\ahk"

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
