import curses
import sys
import math
import numpy

sys.path.append("../labwork2")

from OOP_student_mark import *

class Mark_Manager:
    def __init__(self, name):
        self.name = name
    
    def round_down(self, name) -> int:
        print("ROUND-DOWN Marks")
        for _ in range(ls.__len__()):
            if name == ls[_].name:
                for subject in ls[_].course:
                    print(f"Mark of {subject[0]} round-down to: { math.floor(float(subject[1])) }")
     
    def GPA(self, name) -> tuple:
        for _ in range(ls.__len__()):
            if name == ls[_].name:
                
                GPA = numpy.mean([float(i[1]) for i in ls[_].course])
                print(f"GPA's {name} is : { GPA }")
            
                return tuple((GPA ,name))
    def sort_by_GPA(self) -> str:
        
        GPA_list = [self.GPA(ls[_].name) for _ in range(len(ls)) ]
    
        descending = sorted(GPA_list, key=lambda i: i[1])
                
        for top,value in enumerate(descending):
            print(f"Ranking {top+1} is {value[0]} with {value[1]} points")

t = Mark_Manager('Aiden',)
t.round_down('Aiden')
t.GPA('Aiden')
t.sort_by_GPA()