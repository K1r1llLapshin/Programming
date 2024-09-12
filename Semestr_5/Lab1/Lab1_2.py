from pathlib import Path
import argparse
import os
# Создал парсет с двумя аргументами 
parser = argparse.ArgumentParser() 
parser.add_argument('--dirpath', default=".")
parser.add_argument('--file', nargs="*")
#--------------------------------------------

dirpath_ = parser.parse_args().dirpath # путь к папке 
files_ = parser.parse_args().file # файлы, которые проверяем

if files_: # Если файлы есть, то проверяем какие есть в папке, а ких нет
    found_files = []
    not_found_files = []
    for file in files_:
        if  os.path.exists(os.path.join(dirpath_, file)):
            found_files.append(file)
        else:
            not_found_files.append(file) 
                            
    with open("C:/found_file.txt", "w") as f, open("C:/not_found_file.txt", "w") as n_f: #записываем результаты в файлы 
        f.write("\n".join(found_files) + "\n")
        n_f.write("\n".join(not_found_files) + "\n")
    
    print("Присутсвуют файлы:\n", "\n".join(found_files) + "\n", "Не присутсвуют файлы:\n", "\n".join(not_found_files) + "\n")   
                       
else: # если не было указано файлы просто выводим общюю информацию 
    size_files = 0
    files = list(Path(dirpath_).glob("*.*"))
    for file in files:
        size_files += Path(file).stat().st_size
    print("Количество файлов:", len(files), "\nОбщий размер:", size_files, "байт")
  
