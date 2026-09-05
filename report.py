import numpy as np
from database import get_connection
from prediction import predict_performance
def student_report():
    print('\n       STUDENT PERFORMANCE REPORT      \n')
    try:
        student_id = int(input('Enter Student ID: '))
    except ValueError:
        print('Enter valid ID')
        return
    connection = get_connection()
    try:
        cursor = connection.cursor()
        # student details
        cursor.execute(f'select student_id,student_name,age,gender,class_name,attendance,study_hours from students where student_id = {student_id}')
        student = cursor.fetchone()
        student_id = student[0]
        student_name = student[1]
        age = student[2]
        gender = student[3]
        class_name = student[4]
        attendance = float(student[5])
        study_hours = float(student[6])
        # subject-wise marks
        cursor.execute(f'select sub.subject_name,m.marks from marks m join subjects sub on m.subject_id = sub.subject_id where student_id = {student_id} order by sub.subject_id')
        records = cursor.fetchall()
        # marks storing
        marks = []
        for i in records:
            marks.append(float(i[1]))
        marks_array = np.array(marks)
        # statistics calculation
        average_marks = np.mean(marks_array)
        median_marks = np.median(marks_array)
        highest_marks = np.max(marks_array)
        lowest_marks = np.min(marks_array)
        standard_deviation = round(np.std(marks_array),2)
        # Performance prediction 
        performance = predict_performance( average_marks, attendance, study_hours )
        # display report 
        print('\n')
        print('='*50)
        print('     STUDENT PERFORMANCE REPORT      ')
        print('='*50)
        print('Student ID       :',student_id)
        print('Student Name     :',student_name)
        print('Age              :',age)
        print('Gender           :',gender)
        print('Class            :',class_name)
        print('Attendance       :',attendance)
        print('Studey hours     :',study_hours)
        print('\n')
        print('SUBJECT MARKS')
        print('\n')
        for i in records:
            print(f'Subject Name : {i[0]} | Marks : {i[1]}')
        print('\n')
        print('     STATISTICS      ')
        print('\n')
        print('Average marks :',round(average_marks,2))
        print('Median Marks :',round(median_marks,2))
        print('Highest Marks :',highest_marks)
        print('Lowest Marks :',lowest_marks)
        print('Standard Deviation :',standard_deviation)
        print('\n')
        print('     PERFORMANCE PREDICTION      ')
        print('\n')
        print('Predicted Performance: ',performance)
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()