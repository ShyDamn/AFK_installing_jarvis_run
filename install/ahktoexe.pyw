import os
import subprocess

# Путь к директории, содержащей .ahk файлы
ahk_dir = r'C:\jarvis-app\commands\run\ahk'

# Получение списка .ahk файлов
ahk_files = [f for f in os.listdir(ahk_dir) if f.endswith('.ahk')]

# Компиляция .ahk файлов с помощью AutoHotkey
for ahk_file in ahk_files:
    input_file_path = os.path.join(ahk_dir, ahk_file)
    output_file_path = os.path.splitext(input_file_path)[0] + '.exe'
    subprocess.run(['C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe', '/in', input_file_path, '/out', output_file_path])
