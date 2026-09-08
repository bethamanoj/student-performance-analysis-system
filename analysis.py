import numpy as np
from database import get_connection

# Student averege
def student_avg():
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f'''
select s.student_id,s.student_name,round(avg(m.marks),2) as average_marks
from students s join marks m
on s.student_id = m.student_id
group by s.student_id,s.student_name
order by s.student_id
        ''')
        records = cursor.fetchall()
        for i in records:
            print(i)
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()

# Top performing students
def top_students():
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f'''
        select s.student_id,s.student_name,round(avg(m.marks),2) as average_marks
        from students s join marks m
        on s.student_id = m.student_id
        group by s.student_id,s.student_name
        order by average_marks desc
        LIMIT 5
        ''')
        record = cursor.fetchall()
        for i in record:
            print(i)
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()

# subject analysis
def subject_analysis():
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f'''
        select sub.subject_name,round(avg(m.marks),2) as average_marks,max(m.marks) as highest_marks,min(m.marks) as lowest_marks
        from marks m join subjects sub
        on m.subject_id = sub.subject_id
        group by sub.subject_id,sub.subject_name
        order by average_marks desc
        ''')
        records = cursor.fetchall()
        for i in records:
            print(f'''
            Subject : {i[0]}
            Average : {i[1]}
            Highest : {i[2]}
            Lowest : {i[3]}
            ''')
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()

# numpy statistics
def numpy_statistics():
    try:
        student_id = int(input('Enter student ID: '))
    except ValueError:
        print('Enter valid ID')
        return
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = """ SELECT s.student_name, sub.subject_name, m.marks FROM marks m 
        JOIN students s ON m.student_id = s.student_id 
        JOIN subjects sub ON m.subject_id = sub.subject_id 
        WHERE m.student_id = %s 
        ORDER BY sub.subject_id """ 
        cursor.execute(query, (student_id,))
        records = cursor.fetchall()
        student_name = records[0][0]
        print(f'Student Name : {student_name}')
        marks = []
        for record in records: 
            subject_name = record[1] 
            mark = float(record[2]) 
            print(f'{subject_name:<20}: {mark}') 
        marks.append(mark)
        marks_array = np.array(marks)
        print('\n   STATISTICS  ')
        print('Average              :',round(np.mean(marks_array),2))
        print('Meadian              :',round(np.median(marks_array),2))
        print('Highest              :',np.max(marks_array))
        print('Lowest               :',np.min(marks_array))
        print('Standard Deviation   :',round(np.std(marks_array),2))
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()