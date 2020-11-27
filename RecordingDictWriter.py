import csv
 
with open('RecordingDictWriter.csv', 'w') as csvfile:
    fieldnames = ['Service', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
 
    writer.writeheader()
    writer.writerow({'Service': 'Pedicure', 'price': '4200'})
    writer.writerow({'Service': 'Face cleaning',
                     'price': '5000'})
    writer.writerow({'Service': 'A haircut', 'price': '2700'})
    writer.writerow({'Service': 'Massage', 'price': '2500'})
 
print("Writing complete")