
import mysql.connector

class my_db:
    def __init__(self):

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="task2_asli"
        )

    def get_users(self):
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        self.mydb.commit()
        return myresult

    def login_page(self, username, password):
        mycursor = self.mydb.cursor()
        sql = "SELECT idu, name, username, password FROM user where username = %s and password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        self.mydb.commit()
        return myresult

    def check_password(self, username, password):
        users = self.login_page(username, password)
        for user in users:
            if username == user[2] and password == user[3]:
                return True
            return False

    def add_task(self, idu, task, idt):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO tasks (idu, idt, task) VALUES (%s, %s, %s)"
        val = (idu, idt, task)
        mycursor.execute(sql, val)
        self.mydb.commit()

    def show_value(self, user_name):
        mycursor = self.mydb.cursor()
        # idu, idt, task
        sql = f"SELECT idt, task FROM tasks, user where tasks.idu = user.idu AND user.name = %s"
        val = (user_name, )
        mycursor.execute(sql, val)

        myresult = mycursor.fetchall()
        return myresult

    def update_value(self, new_task, number_task, user_name):
        mycursor = self.mydb.cursor()
        sql = "UPDATE tasks SET task = (%s) WHERE idt = (%s) and idu = (select idu from user where name = %s)"
        val = (new_task, number_task, user_name)
        mycursor.execute(sql, val)

        self.mydb.commit()
        return mycursor.rowcount, "record(s) affected"

    def delete_value(self, number_task):
        mycursor = self.mydb.cursor()

        sql = "DELETE FROM tasks WHERE idt = (%s)"
        val = (number_task,)

        mycursor.execute(sql, val)

        self.mydb.commit()

        return mycursor.rowcount, "record(s) deleted"









# # select
# for x in myresult:
#   print(x)
# insert in table
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO user (idu, name, username, password) VALUES (%s, %s, %s, %s)"
# val = (2, "kimia", "kimi", "5678")
# mycursor.execute(sql, val)
#
# mydb.commit()
#\
# print(mycursor.rowcount, "record inserted.")


# creat table
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE user (idu int, name VARCHAR(255), username VARCHAR(16), password VARCHAR(13))")
# print("TABLE created successfully")
# mydb.close()
# mycursor.close()
