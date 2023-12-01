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


def main():
    connection = connect()
    print("Get the list Of doctors as per the given specialty and salary \n")
    get_specialist_doctors_list("Garnacologist", 30000, connection)
    connection.close()


if __name__ == "__main__":
    main()

"""
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

def get_specialist_doctors_list(speciality, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = "select *
                            from Doctor where Speciality=%s and Salary > %s"
        cursor.execute(sql_select_query, (speciality, salary))
        records = cursor.fetchall()
        print("Printing doctors whose specialty
               is", speciality, "and salary greater than", salary, "\n")
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 3: Get Doctors as per given Speciality\n")
get_specialist_doctors_list("Garnacologist", 30000)
"""
