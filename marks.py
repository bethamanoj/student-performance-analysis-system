from database import get_connection

# add marks
def add_marks():
    try:
        student_id = int(input('Enter Student ID: '))
        subject_id = int(input('Enter subject ID: '))
        marks = float(input('Enter Marks: '))
        if marks>100 or marks<0:
            print('Marks must be between 0 and 100')
            return
    except ValueError:
        print('Please enter valid values')
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f'select student_id from students where student_id = {student_id}')  #check student
        student = cursor.fetchone()
        if student is None:
            print('Student id not found')
            return
        cursor.execute(f'select subject_id from subjects where subject_id = {subject_id}')  #check subject
        subject = cursor.fetchone()
        if subject is None:
            print('Subject not found')
            return
        cursor.execute(f'insert into marks (student_id,subject_id,marks) values({student_id},{subject_id},{marks})')
        connection.commit()
        print('Marks added successfully')
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()

# view marks
def view_marks():
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f'''select m.mark_id,s.student_name,sub.subject_name,m.marks 
        from marks m 
        join students s 
        on m.student_id = s.student_id
        join subjects sub
        on m.subject_id = sub.subject_id
        order by s.student_id,sub.subject_id
        ''')
        records = cursor.fetchall()
        if not records:
            print('No marks found')
            return
        for i in records:
            print(i)
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()

# Search student marks
def search_student_marks():
    try:
        student_id = int(input('Enter student ID: '))
    except ValueError:
        print('Enter valid student ID')
        return
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f'''
        select s.student_name,sub.subject_name,m.marks
        from marks m join students s
        on m.student_id = s.student_id
        join subjects sub
        on m.subject_id = sub.subject_id
        where s.student_id = {student_id}
        order by sub.subject_id
        ''')
        records = cursor.fetchall()
        if not records:
            print('No marks found')
            return
        print('\nStudent:',records[0][0])
        print()
        for i in records:
            print(f'{i[1]} : {i[2]}')
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()
