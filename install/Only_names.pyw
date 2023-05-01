import re

with open('all_directory.txt', 'r', encoding='Windows-1251') as f:
    lines = f.readlines()

names = []

for line in lines:
    parts = line.split('\\')
    name = parts[-1].replace('.lnk', '')
    name = re.sub(r'\(.*?\)', '', name)
    name = re.sub(r'[\d\W]+', ' ', name)
    name = ' '.join(name.split())
    if name not in names:
        names.append(name)

with open('only_names.txt', 'w', encoding='Windows-1251') as f:
    f.write('\n'.join(names))
