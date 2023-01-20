import mysql.connector
# import mysql.connector
# from mysql.connector import errorcode

# try:
#     mydb = mysql.connector.connect(
#         user='root',
#         password="@26102000",
#         host="127.0.0.1"
#     )
#     my_cursor = mydb.cursor()

#     # my_cursor.execute("CREATE DATABASE our_users")

#     my_cursor.execute("SHOW DATABASES")
#     for db in my_cursor:
#         print(db)

# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#     mydb.close()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@26102000",

)


my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE our_users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
