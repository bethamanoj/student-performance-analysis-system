from database import get_connection
# add student 
def add_student():
    try:
        name = input('Enter student name: ')
        if name == '':
            print('Student name cannot be empty')
            return
        age = int(input('Enter age: '))
        if age <= 0:
            print('Age must be greater than 0.')
            return
        gender = input("Enter gender: ")
        class_name = input("Enter class: ")
        attendance = float(input("Enter attendance percentage: "))
        if attendance<0 or attendance>100:
            print('Attendance must be in between 0 and 100')
        study_hours = float(input("Enter daily study hours: "))
        if study_hours < 0:
            print('Study hours cannot be negative.')   
    except ValueError:
        print('Please enter valid values.')
        return
    connection = get_connection()
    if connection is None:
        return
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(f"insert into students(student_name,age,gender,class_name,attendance,study_hours) values('{name}',{age},'{gender}','{class_name}',{attendance},{study_hours})")
        connection.commit()
        print('Student added successfully')
    except Exception as error:
        print('Error: ',error)
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()

# view students
def view_students():
    connection = get_connection()
    if connection is None:
        return
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("select * from students order by student_id")
        students = cursor.fetchall()
        print('\n   Students    \n')
        for i in students:
            print(i)
    except Exception as error:
        print('Error:',error)
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()

# search student
def search_student():
    name = input('Enter student name: ')
    connection = get_connection()
    if connection is None:
        return
    cursor = None
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM students WHERE student_name LIKE %s"
        cursor.execute(query, (f"%{name}%",))
        students = cursor.fetchall()
        if students:
            for student in students:
                print(student)
        else:
            print('No student Record')
    except Exception as error:
        print('Error:', error)
    finally:
        if cursor:
            cursor.close()
        connection.close()

# update student
def update_student():
    try:
        student_id = int(input('Enter Student ID: '))
    except ValueError:
        print('Please enter valid ID')
        return
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f'select * from students where student_id = %s',(student_id,))
        student = cursor.fetchone()
        print('\nEnter new details')
        name = input('Engter student name: ')
        if name == '':
            print('Name cannot be empty')
            return
        age = int(input('Enter student age: '))
        if age<=0:
            print('Age must be greater than 0')
            return
        gender = input("Enter gender: ")
        class_name = input("Enter class: ")
        attendance = float(
            input("Enter attendance percentage: ")
        )
        if attendance < 0 or attendance > 100:
            print("Attendance must be between 0 and 100.")
            return
        study_hours = float(
            input("Enter daily study hours: ")
        )
        if study_hours < 0:
            print("Study hours cannot be negative.")
            return  
        query = """ UPDATE students SET student_name = %s, age = %s, gender = %s, class_name = %s, attendance = %s, study_hours = %s WHERE student_id = %s """ 
        values = ( name, age, gender, class_name, attendance, study_hours, student_id ) 
        cursor.execute(query, values)
        connection.commit()
        print('Student updated successfully')
    except ValueError:
        print('Enter valid values')
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()

# delete student
def delete_student():
    try:
        student_id = int(input('Enter student id: '))
    except ValueError:
        print('Enter valid ID')
        return
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f'select student_name from students where student_id = {student_id}')
        student = cursor.fetchone()
        print('Student:',student[0])
        confirm = input('Are you sure to delete this student(yes/no): ')
        if confirm != 'yes':
            print('Deletion cancelled')
            return
        cursor.execute(f'delete from marks where student_id = {student_id}')
        cursor.execute(f'delete from students where student_id = {student_id}')
        connection.commit()
        print('Student Deleted Successfully')
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()

