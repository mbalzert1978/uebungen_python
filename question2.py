import mysql.connector
from mysql.connector import Error


def connect():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='python_db',
                                             user='root')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection

    except Error as e:
        print("Error while connecting to MySQL", e)


def get_hospital_detail(hospital_id, connection):
    cursor = connection.cursor()
    cursor.execute(f"select * from Hospital where Hospital_Id= {hospital_id};")
    for item in cursor.fetchall():
        print("Printing Hospital record")
        print(f"Hospital Id: {item[0]}")
        print(f"Hospital Name: {item[1]}")
        print(f"Bed Count: {item[2]}")
    cursor.close()
    return
    # Read data from Hospital table


def get_doctor_detail(doctor_id, connection):
    cursor = connection.cursor()
    cursor.execute(f"select * from Doctor where Doctor_Id= {doctor_id};")
    for item in cursor.fetchall():
        datetimestr = item[3].strftime("%d.%m.%Y")
        print("Printing Doctor record")
        print(f"Doctor Id: {item[0]}")
        print(f"Doctor Name: {item[1]}")
        print(f"Hospital Id: {item[2]}")
        print(f"Joining Date: {datetimestr}")
        print(f"Specialty: {item[4]}")
        print(f"Salary: {item[5]}")
        print(f"Experience:{item[6]}")
    cursor.close()
    return
    # Read data from Doctor table


def main():
    connection = connect()
    print("Question 2: Read given hospital and doctor details \n")
    get_doctor_detail(105, connection)
    get_hospital_detail(2, connection)
    connection.close()


if __name__ == "__main__":
    main()


""" Musterlösung
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='pynative',
                                         password='pynative@#29')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_hospital_detail(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = "select * from Hospital where Hospital_Id = %s"
        cursor.execute(select_query, (hospital_id,))
        records = cursor.fetchall()
        print("Printing Hospital record")
        for row in records:
            print("Hospital Id:", row[0], )
            print("Hospital Name:", row[1])
            print("Bed Count:", row[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctor_detail(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = "select * from Doctor where Doctor_Id = %s"
        cursor.execute(select_query, (doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor record")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 2: Read given hospital and doctor details \n")
get_hospital_detail(2)
print("\n")
get_doctor_detail(105)
"""
