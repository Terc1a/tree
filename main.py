import os

# Указываем путь к директории
directory = f"C:/Users/Terc1a/Desktop/ziq/"
content = os.listdir(directory)
# Получаем список файлов

files1 = []
# Добавляем файлы в список
# Выводим список файлов
for file in content:
    if os.path.isfile(os.path.join(directory, file)) and file.endswith('.md'):
        files1.append(file)
# print(files1)

with os.scandir(directory) as files:
    for file in files:
        pass
        #print(file.name)


