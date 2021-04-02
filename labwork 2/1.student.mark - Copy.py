import json
import pandas as pd
from collections import Counter

student_list = []

def select_course(nums):

    course_list = {}
    
    dict_courses = {
        1: "Advanced Python",
        2: "Signal and System",
        3: "IPM",
        4: "FRENCH"
    }

    print("""
        Courses that you can select:
        1.Advanced Python 
        2.Signal and System
        3.IPM
        4.FRENCH
        """)

    for i in range(nums):
        course = int(input(f'select the {i+1} course : '))
        mark = int(input(f'your fukin mark for {dict_courses.get(course)} : '))
        course_list[dict_courses.get(course)] = mark
        
    return course_list

def input_func(nums):
    for i in range(nums):
        
        try:
            each_student = {}

            name = str(input('Name: '))
            sid = int(input('ID: '))
            dob = str(input('Date Of Birth: '))

            each_student['Name'] = name
            each_student['ID'] = sid
            each_student['BoD'] = dob

            course = input('Input the fukin number(how many course you want) : ')
    #         course = 2 

            each_student['course'] = select_course(nums)

            student_list.append(each_student)
        except Exception as e:
            print('ERROR',e)
            print('Something not right, plz enter again')
            input_func(nums)

def listing():
    ls = []
    print('Total student :',len(student_list))
    print('List Student :',','.join(list(student_list[_]['Name'] for _ in range(len(student_list)))))
    
    for _ in range(len(student_list)):
        ls1 = [ls.append(i) for i in list(student_list[_].get('course'))]
    total_course = Counter(ls)
    
    for i in range(len(total_course)):
        print(f'Number of Student register {list(total_course.keys())[i]} : {total_course[list(total_course.keys())[i]]}')
        
    
    try:
        get_mark = input('Get all Student Mark in course : ') 
        # get_mark = 'FRENCH'
    
        print(f'List of students marks in {get_mark}')
        for i in student_list:
            if get_mark in i['course']:
                print(i['Name'] + ': ' + str(i['course'][get_mark]) )
    except Exception as e: 
        print('No one Study this course')
        print('ERROR',e)
    

# nums_of_student = 2
nums_of_student = int(input('Number of Students : ') )
input_func(nums_of_student)
listing()  