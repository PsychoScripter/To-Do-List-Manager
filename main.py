from pythonProject1.time import Time
from query import my_db
from banner import banner

qq = my_db()
response = qq.get_users()
print(response)
#
# table.show_table()
# response = table.create_table()
# print(response)
banner()
time_now = Time().time_now()
print("Wellcome, please login...")
while True:
    logname = input("username:\n")
    logpassword = input("password:\n")
    if qq.check_password(logname, logpassword):
        print("login successful\n")

        break
    else:
        print("wrong")
# '''user_name = {idu , name, username, password} logged'''

user_name = qq.login_page(logname, logpassword)
for name_login in user_name:
    name = name_login[1]
name_str = ''.join(name)
print(f"Hello {name}, what do you want to do?")
while True:
    user_choices = input(
                         "1. Add Task"
                         "\n2. View Tasks"
                         "\n3. Update Task"
                         "\n4. Delete Task"
                         "\n5. Quite"
                         "\nChoose a number: ")
    if user_choices == "1":
        for idm in user_name:
            id_user = idm[0]

        while True:
            #check for input integer
            while True:
                try:
                    id_task = int(input("Enter id task:"))
                    break
                except ValueError:
                    print("invalid input(please enter an integer)")

            user_task = input("Enter your task: ")
            if user_task is not None:
                result = qq.add_task(idt=id_task, idu=id_user, task=user_task)
                print("Task added\n")
                break
            else:
                print("Invalid\n")

    elif user_choices == "2":
        show_value = qq.show_value(user_name=name_str)
        print(show_value)
        print("\n")

    elif user_choices == "3":
        print("This is your tasks...")
        show_value = qq.show_value(user_name=name_str)
        print(show_value)
        print("\n")

        num_task = input("Enter number of task for update: ")
        new_task = input("Update your task: ")
        update_value = qq.update_value(user_name=name_str, new_task=new_task, number_task=num_task)
        print("Task updated\n")

    elif user_choices == "4":
        print("This is your tasks...")
        show_value = qq.show_value(user_name=name_str)
        print(show_value)
        print("\n")

        num_task = input("Enter number of task for delete: ")
        # y_or_n
        y_or_n = input("Are you sure you want to delete this task? (y/n): ")
        if y_or_n == "y":
            delete_value = qq.delete_value(number_task=num_task)
        print("Task deleted\n")
    elif user_choices == "5":
        print("Good bye")
        break
    else:
        print("Invalid")
