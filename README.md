# Student Performance Analysis & Prediction System

## Overview

The Student Performance Analysis & Prediction System is a Python and MySQL based application for managing student information, subject-wise marks, attendance, and study hours.

The system analyzes student performance using SQL and NumPy and predicts performance based on predefined conditions.

## Technologies Used

* Python
* MySQL
* SQL
* NumPy

## Features

* Add students
* View students
* Search students
* Update student information
* Delete students
* Add subject-wise marks
* View marks
* Calculate student average
* Find top performing students
* Perform subject-wise analysis
* Calculate statistical values using NumPy
* Predict student performance
* Generate student performance report

## Database

The project uses MySQL with three main tables:

### Students

Stores student information such as:

* Student ID
* Student Name
* Age
* Gender
* Class
* Attendance
* Study Hours

### Subjects

Stores subject information such as:

* Subject ID
* Subject Name

### Marks

Stores:

* Mark ID
* Student ID
* Subject ID
* Marks

Foreign keys are used to connect the marks records with students and subjects.

## SQL Concepts Used

* INSERT
* SELECT
* UPDATE
* DELETE
* JOIN
* GROUP BY
* ORDER BY
* LIMIT
* AVG
* MAX
* MIN
* COUNT
* Primary Key
* Foreign Key

## NumPy Concepts Used

* Array
* Mean
* Median
* Maximum
* Minimum
* Standard Deviation

## Performance Prediction

The system predicts student performance using predefined rules based on:

* Average marks
* Attendance
* Study hours

The performance categories are:

* Excellent
* Good
* Average
* Needs Improvement

## How to Run

Install the required packages:

```text
pip install -r requirements.txt
```

Create the MySQL database and tables.

Configure the database credentials locally in `database.py`.

Do not upload your actual MySQL password to GitHub.

Run:

```text
python main.py
```

## Future Improvements

* Add a graphical user interface
* Add data visualization
* Add PDF or Excel report generation
* Add student login
* Add machine learning-based performance prediction
