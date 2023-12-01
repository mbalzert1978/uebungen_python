import datetime
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


def get_specialist_doctors_list(speciality, salary, connection):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT *                          \
          FROM Doctor                       \
          WHERE Speciality= '{speciality}'  \
          AND Salary > '{salary}';")
    if temp := cursor.fetchall():
        print(f"Printing doctors whose specialty \
is {speciality} and salary greater than {salary} ")
        for item in temp:
            datetimestr = item[3].strftime("%d.%m.%Y")
            print(f"Doctor Id: {item[0]}")
            print(f"Doctor Name: {item[1]}")
            print(f"Hospital Id: {item[2]}")
            print(f"Joining Date: {datetimestr}")
            print(f"Specialty: {item[4]}")
            print(f"Salary: {item[5]}")
            print(f"Experience:{item[6]}")
    else:
        print("No Data")
    cursor.close()
    return
    # Fetch doctor's details as per Speciality and Salary


def get_doctors(hospital_id, connection):
    cursor = connection.cursor()
    cursor.execute(
        f"select * from Doctor where Hospital_Id= {hospital_id};")
    temp = cursor.fetchall()
    hospital_name = get_hospital_name(hospital_id, connection)
    if temp:
        for item in temp:
            d_id, d_name, h_id, j_date, spec, sal, *exp = item
            if type(j_date) == datetime.date:
                j_date = j_date.strftime("%d.%m.%Y")
            print("Printing Doctor record")
            print(f"works at {hospital_name}")
            print(f"Doctor Id: {d_id}")
            print(f"Doctor Name: {d_name}")
            print(f"Hospital Id: {h_id}")
            print(f"Joining Date: {j_date}")
            print(f"Specialty: {spec}")
            print(f"Salary: {sal}")
            print(f"Experience:{exp}\n")
    else:
        print("No Data")
    cursor.close()
    return


def get_hospital_name(hospital_id, connection):
    cursor = connection.cursor()
    cursor.execute(
        f"select Hospital_Name from Hospital where Hospital_Id={hospital_id};")
    hospital_name = cursor.fetchone()[0]
    cursor.close()
    return hospital_name
    # Read data from Hospital table


def main():
    connection = connect()
    print("Get a list of doctors from a given hospital \n")
    get_doctors(2, connection)
    connection.close()


if __name__ == "__main__":
    main()

""" Muster
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

def get_hospital_name(hospital_id):
    # Fetch Hospital Name using Hospital id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = "select * from Hospital where Hospital_Id = %s"
        cursor.execute(select_query, (hospital_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctors(hospital_id):
    # Fetch Hospital Name using Hospital id
    try:
        hospital_name = get_hospital_name(hospital_id)
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = "select * from Doctor where Hospital_Id = %s"
        cursor.execute(sql_select_query, (hospital_id,))
        records = cursor.fetchall()

        print("Printing Doctors of ", hospital_name, "Hospital")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)

print("Question 4:  Get List of doctors of a given Hospital Id\n")
get_doctors(2)
"""
