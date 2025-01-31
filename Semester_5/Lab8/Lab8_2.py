from peewee import *

db = SqliteDatabase('delivery.db')

class Courier(Model):
    id_courier = IntegerField(primary_key=True)
    Surname = TextField()
    First_name = TextField() 
    Second_name = TextField()
    Date_of_birth = TextField()
    Date_of_employment = TextField()
    Start_of_working_day = TextField()
    End_of_working_day  = TextField()
    City = TextField()
    Street = TextField()
    House = TextField()
    Apartment = TextField()
    Phone = TextField()
    
    class Meta:
        database = db

class Transport(Model):
    Car_number = TextField(primary_key=True)
    Make = TextField()
    Registration_date = TextField()
    Color = TextField()
    
    class Meta:
        database = db

class Mailer(Model):
    id_mailer = IntegerField(primary_key=True)
    Surname = TextField()
    First_name = TextField() 
    Second_name = TextField()
    Date_of_birth = TextField()
    Index_ = TextField()
    City = TextField()
    Street = TextField()
    House = TextField()
    Apartment = TextField()
    Telephone = TextField()
    
    class Meta:
        table_name = 'maile'
        database = db
        
class Recipient(Model):
    id_recipient = IntegerField(primary_key=True)
    Surname = TextField()
    First_name = TextField() 
    Second_name = TextField()
    Date_of_birth = TextField()
    Index_ = TextField()
    City = TextField()
    Street = TextField()
    House = TextField()
    Apartment = TextField()
    Telephone = TextField()
    
    class Meta:
        table_name = 'recipient'
        database = db


class Order(Model):
    id_order = IntegerField(primary_key=True)
    id_mailer = ForeignKeyField(Mailer, backref='orders')
    id_recipient = ForeignKeyField(Recipient, backref='orders')
    Order_date = TextField()
    Delivery_date = TextField()
    Delivery_price = IntegerField()
    id_courier = ForeignKeyField(Courier, backref='orders')
    Car_number = ForeignKeyField(Transport, backref='orders')
    
    class Meta:
        database = db
        
Courier.create_table()
Transport.create_table()
Order.create_table()

Courier.create(id_courier = 1, 
               Surname = 'Иванов', 
               First_name = 'Кирилл', 
               Second_name = 'Фёдорович', 
               Date_of_birth = '12.12.2000', 
               Date_of_employment = '23.10.2022', 
               Start_of_working_day = '9:30',
               End_of_working_day  = '20:00',
               City = 'Москва',
               Street = 'Кузьмина',
               House = '43Б',
               Apartment = '25',
               Phone = '+7 (954) 132-52-45')

Courier.create(id_courier = 2, 
               Surname = 'Калугина', 
               First_name = 'Алина', 
               Second_name = 'Генадьевна', 
               Date_of_birth = '14.07.1993', 
               Date_of_employment = '21.09.2023', 
               Start_of_working_day = '10:00',
               End_of_working_day  = '20:00',
               City = 'Казань',
               Street = 'генерала Мышкина',
               House = '2',
               Apartment = '20',
               Phone = '+7 (944) 176-52-99')

Transport.create(Car_number = 'А345ВА',
                 Make = 'Audi',
                 Registration_date = '11.11.1999',
                 Color = 'черный')

Transport.create(Car_number = 'А999АА',
                 Make = 'Mercedes',
                 Registration_date = '18.01.2001',
                 Color = 'красный')

Order.create(id_order = 1,
             id_mailer = 1,
             id_recipient = 2,
             Order_date = '20.04.2024',
             Delivery_date ='20.05.2024',
             Delivery_price = 1300,
             id_courier = 1,
             Car_number = 'А345ВА')

Order.create(id_order = 2,
             id_mailer = 2,
             id_recipient = 1,
             Order_date = '21.11.2024',
             Delivery_date ='26.11.2024',
             Delivery_price = 20000,
             id_courier = 2,
             Car_number = 'А999АА')