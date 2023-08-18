import mysql.connector
from properties import *
conn = mysql.connector.connect(host=host, database=database,
                        user=user,password=password)

assert conn.is_connected() == True

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')


rows = cursor.fetchall()
print(rows)
sum = 0
for row in rows:  #('selenium', datetime.date(2020, 6, 7), 120, 'Africa')
    sum = sum + row[2]

print(sum)
assert sum == 722

query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK","Jmeter")
conn.commit()









conn.close()
