import os
directory = f"C:/Users/Terc1a/Desktop/ziq/"
content = os.listdir(directory)
files = []
dirs = []

for file in content:
    if os.path.isfile(os.path.join(directory, file)) and file.endswith('.md'):
        files.append(file)

for dir in content:
    if os.path.isdir(os.path.join(directory, dir)):
        dirs.append(dir)

print(files, 'files')
print(dirs, 'dirs')

for dir_file in dirs:
    if os.path.isfile(os.path.join(directory, dir_file)) and file.endswith('.md'):
        files.append(dir_file)

print(files, 'files inside dir')