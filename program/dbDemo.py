import mysql.connector
from program.config.properties import *


def execute_database_query():
    conn = mysql.connector.connect(host=host, database=database, user=user, password=password)

    assert conn.is_connected() == True

    cursor = conn.cursor()

    cursor.execute('select * from CustomerInfo')
    rows = cursor.fetchall()
    print(rows)

    sum = 0
    for row in rows:
        sum = sum + row[2]

    print(sum)
    assert sum == 722

    query = "update customerInfo set Location = %s where CourseName = %s"
    data = ("UK", "Jmeter")

    cursor.execute(query, data)
    conn.commit()

    conn.close()


# Call the function to execute the database query
if __name__ == "__main__":
    execute_database_query()

