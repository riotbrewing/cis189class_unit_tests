"""
Name: Andrew Steele
Class: CIS 189
Module: 10
Topic: 3
Assignment: Unit Test Class Assignment

Description: Build unit tests for the student class then print two instance of the class
"""
from class_definitions.student import Student

if __name__ == '__main__':
    student_one = Student("Reynolds", "Mal", "Floral Bonnets", 2.9)
    student_two = Student("Solo", "Han", "Smuggling", 3.8)

    print(str(student_one))
    print(str(student_two))
