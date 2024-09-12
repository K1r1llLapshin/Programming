import os
from pathlib import Path
from sys import argv

dir_ = Path(argv[1]) if len(argv[1])> 1 else Path('.')  # Получаем путь из аргументов командной строки, если путь не указан, используем текущую директорию

with open("C:/not_found_file.txt", "r") as nf:
    files = nf.readlines()

for file in files:
    file_name = file.strip() # Удаляем \n в конце 
    new_file_pass = os.path.join(dir_, file_name) # новый путь к файлу
    with open (new_file_pass, "w") as f:
        f.write(' ')