from student import(add_student,view_students,search_student,update_student,delete_student)
from marks import (add_marks,view_marks)
from analysis import (student_avg,top_students,subject_analysis,numpy_statistics)
from prediction import performance_prediction
from report import student_report
while True:
    print('='*50)
    print('     STUDENT PERFORMANCE ANALYSIS    ')
    print('='*50)
    print('1.   Add Student')
    print('2.   View Student')
    print('3.   Search Student')
    print('4.   Update Student')
    print('5.   Delete Student')
    print('6.   Add Marks')
    print('7.   View marks')
    print('8.   Student average')
    print('9.   Top performing Student')
    print('10.  Subject Analysis')
    print('11.  Numpy Statistics')
    print('12.  Performance Prediction')
    print('13.  Student Report')
    print('14.  Exit')

    choice = input('\n Enter the choice: ')
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        add_marks()
    elif choice == '7':
        view_marks()
    elif choice == '8':
        student_avg()
    elif choice == '9':
        top_students()
    elif choice == '10':
        subject_analysis()
    elif choice == '11':
        numpy_statistics()
    elif choice == '12':
        performance_prediction()
    elif choice == '13':
        student_report()
    elif choice == '14':
        print('Thank you')
        break
    else:
        print('Enter Valid Choice.')