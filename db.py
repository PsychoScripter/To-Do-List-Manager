import mysql.connector
# database 'task2_asli'
# table 'duties'
# table 'user'
# table 'tasks'

class CRUD:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="task2_asli"
        )


    def create_db(self, name_database):
        mycursor = self.mydb.cursor()
        try:
            mycursor.execute(f"CREATE DATABASE {name_database}")
            print("Database created successfully")
            self.mydb.commit()
        except Exception as e:
            print("error creat_databasae")
            print('dedlet def....   ' + e)

    def create_table(self):
        mycursor = self.mydb.cursor()
        try:
            mycursor.execute(f"CREATE TABLE Tasks (idu int, idt int, task VARCHAR(255))")
            print("TABLE created successfully")
            self.mydb.commit()
        except Exception as e:
            print("error creat_TABLE")
            print('dedlet def....   ' + e)

    def show_table(self):
        # self.mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="",
        #     database=name_database
        # )
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW TABLES")

        for x in mycursor:
            print(x)

    def show_value(self, table_name):
        mycursor = self.mydb.cursor()

        mycursor.execute(f"SELECT * FROM {table_name}")

        myresult = mycursor.fetchall()
        return myresult


