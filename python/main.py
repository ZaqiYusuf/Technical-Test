import re

host = "localhost"
user = "root"
passwd = ""

import mysql.connector as mysql

db = mysql.connect(
    host = host,
    user = user,
    passwd = passwd
)
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE `mydatabase`.`workers` (
        _id int not null,
        name VARCHAR(255) NOT NULL,
        task VARCHAR(255) NOT NULL,
        hours TIME,
        PRIMARY KEY (_id)
    );
''')
db.commit()
data = cursor.fetchall()
print(data)


name = input("Enter your name : ")
task = input("Enter the number task you want to do : ")

print("==========================================")
print("Please choose your tasks")
print("==========================================")

# print("")

