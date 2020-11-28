import os


files = os.listdir('./saves')
for file in files:
    with open(f'./saves/{file}', 'w', encoding='utf-8') as file:
        if file == 'enemies.json':
            file.write('[]')
        else:
            file.write('{}')
