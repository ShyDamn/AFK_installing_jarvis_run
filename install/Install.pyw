import subprocess

# установка библиотеки yaml
subprocess.check_call(['pip', 'install', 'PyYaml'])

# запуск скриптов по очереди
subprocess.run('python all_directory.pyw', check=True)
subprocess.run('python only_names.pyw', check=True)
subprocess.run('python russian_names.pyw', check=True)
subprocess.run('python YML.pyw', check=True)
subprocess.run('python ahk.pyw', check=True) 
