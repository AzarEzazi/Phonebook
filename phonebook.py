import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "contact"
)
mycursor = mydb.cursor()
class Phonebook:

    def add (self , name , family , phone_number):
        mycursor = mydb.cursor()
        sql = "INSERT INTO contact (name , family , phone_number) VALUES (%s, %s , %s)"
        val = (name , family , phone_number)
        mycursor.execute(sql, val)
        mydb.commit()

    def search (self , search_var ):
        mycursor = mydb.cursor()
        sql = ("SELECT * FROM contact WHERE name = %s OR   family = %s OR  phone_number = %s")
        val = (search_var , search_var , search_var)
        mycursor.execute(sql , val)
        myresult = mycursor.fetchall()
        print(myresult)



    def delete(self , search_var):
        mycursor = mydb.cursor()
        sql = f"DELETE FROM contact WHERE name = '{search_var}' or  family = '{search_var}' or phone_number = '{search_var}' "
        print(sql)
        mycursor.execute(sql)
        mydb.commit()


    def update_info(self,id ,key,value):
        mycursor = mydb.cursor()
        mycursor.execute(f"update contact set {key} = '{value}' where id = {int(id)} ")
        mydb.commit()

    def showall (self):
        mycursor = mydb.cursor()
        mycursor.execute("select * from contact" )
        myresult = mycursor.fetchall()
        print(myresult)
while True:
    command = int(input("1_add \n 2_delete \n 3_search \n 4_edit \n 5_showall\n 6_exit\n"))
    if command == 1 :
        name = input(" name: ")
        family= input("family: ")
        phone_number = input("phone number: ")
        Phonebook().add(name , family , phone_number)
        print('added!')

    elif command == 2 :
        search_var = input("search: ")
        Phonebook().search(search_var)
        Phonebook().delete(search_var)
        print('delete')
    elif command == 3 :
        search_var = input("search: ")
        Phonebook().search(search_var)


    elif command == 4 :
        search_var = input("search: ")
        Phonebook().search(search_var)
        x = int(input("1_name \n 2_family \n 3_phone_number \n "))
        id = input('id: ')

        if x == 1 :
            name = input('name: ')
            Phonebook().update_info(id,key = 'name',value=name)
        if x == 2:
            family = input('family: ')
            Phonebook().update_info(id,key = 'family',value=family)
        if x == 3 :
            phone_number = input('phone_number: ')
            Phonebook().update_info(id,key='phone_number',value=phone_number)

    elif command == 5:
        Phonebook().showall()

    elif command == 6 :
        break