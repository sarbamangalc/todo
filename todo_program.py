import mysql.connector
from mysql.connector import errorcode

#mydb = mysql.connector.connect( host="localhost", user="root", password="Meghai2003", database="todo")
#mydb=mysql.connector.connect(user='root', password='Meghai2003', host='127.0.0.1', database='todo')

def mysqlconnect():
    try:
        cnx = mysql.connector.connect(user='root', password='Meghai2003', host='127.0.0.1', database='todo', auth_plugin='mysql_native_password') 
    except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
             print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
              print("Database does not exist")
          else:
             print(err)



def addTodo():
    mysqlconnect()
    cnx = mysql.connector.connect(user='root', password='Meghai2003', host='127.0.0.1', database='todo', auth_plugin='mysql_native_password') 
    mycursor = cnx.cursor()

    sql = "INSERT INTO item (itemDesc, itemPrice,status) VALUES (%s, %s,%s)"
    itemDesc = raw_input('Enter Item Description: ')
    itemPrice = raw_input('Enter Item Price: ')
    status = raw_input('Enter Item Status: ')
    val = (itemDesc,itemPrice,status)
    mycursor.execute(sql, val)
    cnx.commit()
    print(str(mycursor.rowcount) + " record inserted.")

def deleteTodo():
  try:
      cnx = mysql.connector.connect(user='root', password='Meghai2003', host='127.0.0.1', database='todo', auth_plugin='mysql_native_password') 
      mysqlconnect()
      mycursor = cnx.cursor()
      itemId = raw_input('Enter Item which you want to delete: ')
      sql = "DELETE   FROM ITEM where itemId =" + itemId
      mycursor.execute(sql)
      cnx.commit()
      if mycursor.rowcount == -1:
           print("Record NOT found")
      else:
           print(str(mycursor.rowcount) +  " record deleted.")
 
  except Error as e:
      print(e)
 
  finally:
       mycursor.close()
       cnx.close()

def updateTodo():
  try:
      cnx = mysql.connector.connect(user='root', password='Meghai2003', host='127.0.0.1', database='todo', auth_plugin='mysql_native_password') 
      mysqlconnect()
      mycursor = cnx.cursor()
      itemId = raw_input('Enter ItemId which you want to update: ')
      itemDesc = raw_input('Enter Item description which you want to update: ')
      sql = "UPDATE item  set itemDesc= '" + itemDesc + "' where itemId =" + itemId
      mycursor.execute(sql)
      cnx.commit()
      if mycursor.rowcount == -1:
           print("Record NOT found")
      else:
           print(str(mycursor.rowcount) +  " record Updated.")
 
  except Error as e:
      print(e)
 
  finally:
       mycursor.close()
       cnx.close()

def displayAllTodo():
  try:
      cnx = mysql.connector.connect(user='root', password='Meghai2003', host='127.0.0.1', database='todo', auth_plugin='mysql_native_password') 
      mysqlconnect()
      mycursor = cnx.cursor()
      sql = "SELECT * FROM ITEM"
      mycursor.execute(sql)
      rows= mycursor.fetchall()
      print(str(mycursor.rowcount )+ " record selected.")
      for row in rows:
            print(row)
 
  except Error as e:
       print(e)
 
  finally:
       mycursor.close()
       cnx.close()

def displayOneTodo():
  try:
      cnx = mysql.connector.connect(user='root', password='Meghai2003', host='127.0.0.1', database='todo', auth_plugin='mysql_native_password') 
      mysqlconnect()
      mycursor = cnx.cursor()
      itemId = raw_input('Enter Item Id: ')
      sql = "SELECT * FROM ITEM where itemId =" + itemId
      mycursor.execute(sql)
      row= mycursor.fetchone()
      if mycursor.rowcount == -1:
           print("Record NOT found")
      else:
        print(row)
        print(str(mycursor.rowcount) +  " record selected.")
 
  except Error as e:
       print(e)
 
  finally:
       mycursor.close()
       cnx.close()

ans=True
while ans:
    print("""
    1.Add a Todo
    2.Delete a Todo
    3.Display All Todo  Records
    4.Display One  Todo  Record
    5.Update a Todo
    6.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ")
    if ans=="1":
     addTodo()
    elif ans=="2":
      deleteTodo()
    elif ans=="3":
      displayAllTodo()
    elif ans=="4":
      displayOneTodo()
    elif ans=="5":
      updateTodo()
    elif ans=="6":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")

