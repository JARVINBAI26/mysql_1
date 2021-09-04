from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Jithinbai@2001",database="python_db")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into users(name,age,city) values(%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    con.commit()
    print("data insert success")
def update(name,age,city,id):
    res=con.cursor()
    sql="update users set name=%s,age=%s,city=%s where id=%s"
    user=(name,age,city,id)
    res.execute(sql,user)
    con.commit()
    print("data update success")

def select():
    res=con.cursor()
    sql="select id,name,age,city from users"
    res.execute(sql)
    #result=res.fetchone()
    #result=res.fetchmany(2)
    result=res.fetchall()
    #print(result)
    print(tabulate(result,headers=["id","name","age","city"]))
def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id,)
    res.execute(sql,user)
    con.commit()
    print("data delete success")


while True:
    print("1. insert data")
    print("2. update data")
    print("3. select data")
    print("4. delete data")
    print("5. exit")

    choice=int(input("enter your choice: "))
    if choice==1:
        name=input("enter name: ")
        age=input("enter age: ")
        city=input("enter city: ")

        insert(name,age,city)

    elif choice==2:
        id=input("enter the id: ")
        name=input("enter name: ")
        age=input("enter age: ")
        city=input("enter city: ")

        update(name,age,city,id)
    elif choice==3:
        select()
    elif choice==4:
        id=input("enter the id to delete :")
        delete(id)
    elif choice==5:
        quit()
    else:
        print("invalid selection, please try again!")




