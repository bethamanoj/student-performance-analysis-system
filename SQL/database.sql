create database students_performance;
use students_performance;
create table students(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10),
    class_name VARCHAR(20),
    attendance DECIMAL(5,2),
    study_hours DECIMAL(5,2)
);
create table subjects(
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(100) NOT NULL
);
create table marks (
    mark_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    marks DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (student_id)
    REFERENCES students(student_id),
    FOREIGN KEY (subject_id)
    REFERENCES subjects(subject_id)
);

insert into subjects (subject_name)
values
('Python'),
('SQL'),
('Mathematics'),
('Communication'),
('Aptitude');

insert into students
(student_name, age, gender, class_name, attendance, study_hours)
values
('Rahul Kumar', 21, 'Male', 'B.Tech', 92.00, 5.00),
('Priya Sharma', 22, 'Female', 'B.Tech', 95.00, 6.00),
('Arjun Reddy', 21, 'Male', 'B.Tech', 78.00, 3.00),
('Sneha Rao', 22, 'Female', 'B.Tech', 88.00, 4.00),
('Kiran Kumar', 21, 'Male', 'B.Tech', 70.00, 2.00),
('Anjali Singh', 22, 'Female', 'B.Tech', 91.00, 5.00),
('Vikram Reddy', 21, 'Male', 'B.Tech', 75.00, 3.00),
('Divya Sharma', 22, 'Female', 'B.Tech', 89.00, 4.00),
('Rohit Kumar', 21, 'Male', 'B.Tech', 65.00, 2.00),
('Pooja Rao', 22, 'Female', 'B.Tech', 94.00, 6.00);

insert into marks
(student_id, subject_id, marks)
values
(1,1,88),(1,2,92),(1,3,85),(1,4,90),(1,5,87),
(2,1,95),(2,2,94),(2,3,92),(2,4,96),(2,5,93),
(3,1,72),(3,2,75),(3,3,68),(3,4,78),(3,5,70),
(4,1,85),(4,2,88),(4,3,82),(4,4,90),(4,5,86),
(5,1,58),(5,2,62),(5,3,55),(5,4,68),(5,5,60),
(6,1,91),(6,2,93),(6,3,89),(6,4,94),(6,5,90),
(7,1,70),(7,2,74),(7,3,72),(7,4,76),(7,5,68),
(8,1,86),(8,2,90),(8,3,84),(8,4,88),(8,5,92),
(9,1,55),(9,2,60),(9,3,52),(9,4,65),(9,5,58),
(10,1,94),(10,2,96),(10,3,91),(10,4,95),(10,5,93);