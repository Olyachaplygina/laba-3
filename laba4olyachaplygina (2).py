import sqlite3
### класс "Клиент"
class Client:
    def __init__(self, firsname, lastname, age, phonenumber):
        self.firsname = firsname
        self.lastname = lastname
        self.age = age
        self.phonenumber = phonenumber
### класс "Салон красоты"
class BeautySalon:
   
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost



### подключаемся к базе данных
con = sqlite3.connect('BeautySalon.db')
### создаём курсор для работы с базой данных
cursor = con.cursor()
### создаём таблицу услуг
cursor.execute("""CREATE TABLE salonServices
    (serviceName TEXT NOT NULL, ageInterval TEXT NOT NULL,
    serviceCost TEXT NOT NULL, timeToService TEXT NOT NULL)""")

### добавляем запись
cursor.execute("""INSERT INTO salonServices
    VALUES ('Массаж', '18-35', '2500 руб.', '45 мин.')""")
con.commit()


servicesList = [('Чистка лица', '22-45', '4000 руб.', '35 мин.'), 
                ('Пилинг', '25-30', '1500 руб.', '20 мин.'), 
                ('Маникюр', '18-65', '3200 руб.', '40 мин.'), 
                ('Педикюр', '18-50', '3800 руб.', '50 мин.')]

### добавляем несколько записей
cursor.executemany("""INSERT INTO salonServices VALUES (?, ?, ?, ?)""", servicesList)
con.commit()

### меняем цену
sql = """UPDATE salonServices SET serviceCost='1900 руб.' WHERE serviceName='Пилинг'"""

cursor.execute(sql)
con.commit()

### удаляем данные
sql = """DELETE FROM salonServices WHERE serviceName='Массаж'"""

cursor.execute(sql)
con.commit()

### выводим данные по условию
sql = """SELECT * FROM salonServices WHERE serviceName=?"""

cursor.execute(sql, [("Маникюр")])
print(cursor.fetchall())

### поиск по маске
sql = """SELECT * FROM salonServices WHERE serviceName LIKE '%икюр'"""

cursor.execute(sql)
print(cursor.fetchall())

### конец работы с базой данных

print('Приветсвуем Вас в нашем салоне красоты!')
print('Введите Ваше имя, фамилию, возраст и номер телефона:')

client = Client(firsname=input(), lastname=input(), age=input(), phonenumber=input()) 
print('Вы: ', client.firsname, client.lastname, client.age) 
print('Ваш номер телефона: ', client.phonenumber)


if client.age < '18':
    print('Извините, но в нашем салоне красоты действует ограничение 18+')
    exit(0)
### в переменные service1-4 информация по услуге и стоимости, в service1 будут данные name(массаж) и cost (2500)
service1 = BeautySalon("Массаж", "2500 руб.")
service2 = BeautySalon("Чистка лица", "4000 руб.")
service3 = BeautySalon("Пилинг", "1500 руб.")
service4 = BeautySalon("Маникюр", "3200 руб.")

print('Наш салон красоты предоставляет услуги:')
print('1', service1.name)
print('2', service2.name)
print('3', service3.name)
print('4', service4.name)

print('Какую услугу Вы хотите выбрать?')
service = input() ### переменная service будет хранить в себе то, что мы нажмем с клавиатуры

if service == '1': 
    print('Вы выбрали', service1.name, 'стоимость услуги:', service1.cost)
elif service == '2': 
    print('Вы выбрали', service2.name, 'стоимость услуги:', service2.cost)
elif service == '3': 
    print('Вы выбрали', service3.name, 'стоимость услуги:', service3.cost)
elif service == '4': 
    print('Вы выбрали', service4.name, 'стоимость услуги:', service4.cost)
else: 
    print('Данной услуги не существует')
    
print('Просмотреть другие услуги? Y/N')
answer = input() 


while answer != 'N': ### Циклом проходим, если Y, то выводит услуги, но уже сразу с ценой  

    print('Доступные услуги:')

    print(service1.name, ':', service1.cost)
    print(service2.name, ':', service2.cost)
    print(service3.name, ':', service3.cost)
    print(service4.name, ':', service4.cost)
    
    print('Какую услугу Вы хотите выбрать?')
    service = input()
    if service == '1':
        print('Вы выбрали', service1.name, 'стоимость услуги:', service1.cost)
    elif service == '2':
        print('Вы выбрали', service2.name, 'пстоимость услуги:', service2.cost)
    elif service == '3':
        print('Вы выбрали', service3.name, 'стоимость услуги:', service3.cost)
    elif service == '4':
        print('Вы выбрали', service4.name, 'стоимость услуги:', service4.cost)
    else:
        print('Данной услуги не существует')
    
    print('Просмотреть другие услуги? Y/N')
    answer = input()

if answer == 'N': 
 
    print('Спасибо, что доверяете нам, наши специалисты зделают все в лучшем виде!')
    print('Всего Вам доброго', client.firsname, '!')
    exit(0)
