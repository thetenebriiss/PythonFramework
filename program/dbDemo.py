import mysql.connector
from program.config.properties import *


class DatabaseManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        assert self.conn.is_connected()

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def update_records(self, query, data):
        cursor = self.conn.cursor()
        cursor.execute(query, data)
        self.conn.commit()
        cursor.close()

    def close_connection(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    host = host
    database = database
    user = user
    password = password

    db_manager = DatabaseManager(host, database, user, password)

    try:
        db_manager.connect()

        query = 'select * from CustomerInfo'
        rows = db_manager.execute_query(query)
        print(rows)

        total_sum = sum(row[2] for row in rows)
        print(total_sum)
        assert total_sum == 722

        update_query = "update CustomerInfo set Location = %s where CourseName = %s"
        update_data = ("UK", "Jmeter")
        db_manager.update_records(update_query, update_data)
    finally:
        db_manager.close_connection()

