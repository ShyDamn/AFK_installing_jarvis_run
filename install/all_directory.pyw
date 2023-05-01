import os

start_menu_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
output_file_path = 'all_directory.txt'
exclude_words = ['удаление', 'удалить', 'деинсталлировать', 'uninstall']

with open(output_file_path, 'w') as output_file:
    for root, dirs, files in os.walk(start_menu_path):
        for file in files:
            if file.lower().endswith('.lnk'):
                exclude = False
                for word in exclude_words:
                    if word in file.lower():
                        exclude = True
                        break
                if not exclude:
                    shortcut_path = os.path.join(root, file)
                    target_path = os.path.realpath(shortcut_path)
                    output_file.write(target_path + '\n')

        for sub_dir in dirs:
            subfolder = os.path.join(root, sub_dir)

            for file in os.listdir(subfolder):
                if file.lower().endswith('.lnk'):
                    exclude = False
                    for word in exclude_words:
                        if word in file.lower():
                            exclude = True
                            break
                    if not exclude:
                        shortcut_path = os.path.join(subfolder, file)
                        target_path = os.path.realpath(shortcut_path)
                        output_file.write(target_path + '\n')
