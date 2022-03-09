import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import errorcode

brand = input('Please Insert Your Brand: ')
model = input('Please Insert Your Model: ')
brand = brand.lower()
model = model.lower()

r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/'+brand+'/'+model+'/')

soup = BeautifulSoup(r.text, 'html.parser')
val1 = soup.find_all(class_="font-size-1 text-truncate")

gheymat = []
for car in val1:
    gheymat.append(car.text)

nahaie = []
for i in range(0,len(gheymat)):
    if 'miles' in gheymat[i]:
        nahaie.append(gheymat[i])
nahaie = nahaie[:20]

# print(nahaie)

TABLES = {}
TABLES['truecar'] = (
    "CREATE TABLE `truecar` ("
    "  `miles` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`miles`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='root',
                             password='',
                             host='127.0.0.1',
                             database = 'ara')
cursor = cnx.cursor()


for truecar in TABLES:
    table_description = TABLES[truecar]
    try:
        print("Creating table {}: ".format(truecar), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")



add_car = ("INSERT INTO truecar (miles)VALUES (%s)")


data_car = nahaie
print(data_car)

for i in range(0, len(nahaie)):
    data_car = nahaie[i]
    cursor.execute(add_car, (data_car,))



cnx.commit()
cursor.close()
cnx.close()
