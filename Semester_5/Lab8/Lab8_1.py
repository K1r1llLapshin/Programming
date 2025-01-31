import sqlite3

db = sqlite3.connect('delivery.db')

cursor = db.cursor()
# Создаём таблицы 
cursor.execute('''
                CREATE TABLE IF NOT EXISTS mailer(
                id_mailer INT PRIMARY KEY,
                Surname TEXT,
                First_name TEXT, 
                Second_name TEXT,
                Date_of_birth TEXT,
                Index_ TEXT,
                City TEXT,
                Street TEXT,
                House TEXT,
                Apartment TEXT,
                Telephone TEXT);
            ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS recipient (
                id_recipient INT PRIMARY KEY,
                Surname TEXT,
                First_name TEXT, 
                Second_name TEXT,
                Date_of_birth TEXT,
                Index_ TEXT,
                City TEXT,
                Street TEXT,
                House TEXT,
                Apartment TEXT,
                Telephone TEXT);
                ''')

#Заполняем таблицы данными
cursor.execute('''
               INSERT INTO mailer (id_mailer, Surname, First_name, Second_name, Date_of_birth, Index_, City, Street, House, Apartment, Telephone)
               VALUES ('1', 'Иванов', 'Сергей', 'Алексеевич', '15.03.1985', '101000', 'Москва', 'Тверская', '12А', '15', '+7 (495) 123-45-67');
               ''')

mailer_info = ('2', 'Петрова', 'Марина', 'Николавевна', '22.07.1990', '101032', 'Казань', 'Невский проспект', '25', '30', '+7 (812) 234-56-78 ')
cursor.execute('INSERT INTO mailer VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', mailer_info)

some_recipient_info = [
    ('1', 'Смирнов', 'Дмитрий', 'Иванович', '04.11.2002', '101432', 'Челябинск', 'Невский проспект', '3', '3', '+7 (812) 456-78-90 '),
    ('2', 'Сидорова', 'Наталья', 'Кирилловна', '22.07.2000', '121232', 'Калининград', '9 Апреля', '20', '8', '+7 (456) 123-23-34 ')
]

cursor.executemany('INSERT INTO recipient VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', some_recipient_info)

#Изменяем некоторые данные
cursor.execute('UPDATE recipient SET City = "Казань" WHERE id_recipient = "1" ')
db.commit()

db.close()
