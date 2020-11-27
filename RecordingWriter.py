import csv
 
myData = [["Service", "price"],
          ['Massage', '2500'],
          ['Manicure', '3000'],
          ['Pedicure', '4200']]
 
myFile = open('RecordingWriter.csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(myData)
     
print("Writing complete")