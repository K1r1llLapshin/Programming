from pathlib import Path
from sys import argv
import shutil


dir_ = Path(argv[1]) if len(argv[1]) > 1 else Path('.')  # Получаем путь из аргументов командной строки, если путь не указан, используем текущую директорию
    
files = list(Path(dir_).glob("*.*")) # Создаём список файлов, которые находятся в директории 

for file in files:
    if Path(file).stat().st_size > 2048: # удаляем файлы, которые дольше 2К
        files.remove(file)
        
if files:
    Path("C:/small").mkdir(parents=True, exist_ok=True) # создаём папку small
    for file in files: 
        print(file.name) # выводим названия файлов
        shutil.copy(file, "C:/small/" + file.name) # копируем их в папку small
else:
    print("Файлов нет")
        

