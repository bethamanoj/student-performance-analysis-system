from database import get_connection
def predict_performance(
        average_marks,
        attendance,
        study_hours
):
    if (
        average_marks>=80 and attendance >= 85 and study_hours>=3
    ):
        return 'Excellent'
    elif (average_marks>=60 and attendance>=75):
        return 'Good'
    elif average_marks>= 40:
        return 'Average'
    else:
        return 'Needs Improvement'
def performance_prediction():
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Please enter a valid Student ID.")
        return
    connection = get_connection()
    try:
        cursor = connection.cursor()    # GET STUDENT INFORMATION
        cursor.execute(f'select student_name,attendance,study_hours from students where student_id = {student_id}')
        student = cursor.fetchone()
        student_name = student[0]
        attendance = student[1]
        study_hours = student[2]
        cursor.execute(f'select avg(marks) from marks where student_id = {student_id}')
        result = cursor.fetchone()
        average_marks = float(result[0])
        performance = predict_performance(
            average_marks,
            attendance,
            study_hours
        )
        print('\n   PERFORMANCE RESULT  \n')
        print('Student Name:',student_name)
        print('Average Marks:',round(average_marks,2))
        print('Attendance:',attendance)
        print('Study Hours:',study_hours)
        print('Performance:',performance)
    except Exception as error:
        print('Error:',error)
    finally:
        cursor.close()
        connection.close()