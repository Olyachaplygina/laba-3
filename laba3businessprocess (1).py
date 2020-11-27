
import csv ## библиотеки.cvs
class Client:
    def __init__(self, firsname, lastname, age, phonenumber):
         
        self.firsname = firsname
        self.lastname = lastname
        self.age = age
        self.phonenumber = phonenumber

class BeautySalon:
    def __init__(self, name, cost):
       self.name = name
       self.cost = cost

    def WriterClient(self, client):
        myData = [["FirstName", "LastName", "Age", "Phonenumber", "NameSalone", "Cost"], 
            [client.firsname, client.lastname, client.age, client.phonenumber, self.name, self.cost]] ## передаем наши данные
            
        myFile = open('WriterClient.csv', 'w') 
        with myFile:
            writer = csv.writer(myFile, delimiter=';')
            writer.writerows(myData)
     
###  вторая функция 
    def DictWriterClient(self, client):
        with open('DictWriterClient.csv', 'w') as csvfile:
            fieldnames = ['FirstName', 'LastName', 'Age', 'Phonenumber', 'NameSalone', 'Cost' ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
 
            writer.writeheader()
            writer.writerow({'FirstName': client.firsname, 'LastName': client.lastname, 'Age': client.age, 'Phonenumber': client.phonenumber, 'NameSalone': self.name, 'Cost': self.cost})      


print('Приветсвуем Вас в нашем салоне красоты!')
print('Введите Ваше имя, фамилию, возраст и номер телефона:')

client = Client(firsname=input(), lastname=input(), age=input(), phonenumber=input()) 

print('Вы: ', client.firsname, client.lastname, client.age) 
print('Ваш номер телефона: ', client.phonenumber)

if client.age < '18':
    print('Извините, но в нашем салоне красоты действует ограничение 18+')
    exit(0)

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
service = input() 

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


while answer != 'N': 

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

    print('Спасибо, что пользуетесь нашими услугами!')
    if service == '1':
        print('Запись Ваших данных с помощью csv.writer  .......')
        service1.WriterClient(client) ### сдесь вызываем функцию WriterClient(client) 
        print("Запись прошла успешно!")

    elif service == '2':
        print('Запись Ваших данных с помощью csv.writer  .......')
        service2.WriterClient(client) 
        print("Запись прошла успешно!")

    elif service == '3':
        print('Запись Ваших данных с помощью csv.DictWriter  .......')
        service3.DictWriterClient(client) ## вызываем функцию  DictWriterClient
        print("Запись прошла успешно!")

    elif service == '4':
        print('Запись Ваших данных с помощью csv.DictWriter  .......')
        service4.DictWriterClient(client) 
        print("Запись прошла успешно!")        

    print('Спасибо, что доверяете нам, наши специалисты зделают все в лучшем виде!')

print('Для некоторых клиентов у нас есть доп. услуги и именно Вам мы готовы их предложить')
print('Выберите удобный для Вас формат представления данных: 1. Вывод в колонках 2. Вывод в строках ')

myReaderCSV = input()

if myReaderCSV == '1': 
    with open('Dop.csv') as File: ## открываем файл
        reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL) 
        for row in reader:
            print(row)
elif myReaderCSV == '2': 
    results = []
    with open('Dop.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
    print (results)
else:
    exit(0)