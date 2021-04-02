ls =[]

class Student:
    def __init__(self, name, sid, dob, course):
        self.name   = name
        self.sid    = sid
        self.dob    = dob
        self.course = course
         
    def add(self, name, sid, dob, course): 
        ob = Student(name, sid, dob, course)
        ls.append(ob)
  
    def display(self, ob):
            print(f"""Name : {ob.name}\nStudent ID : {ob.sid}\nDate Of Birth : {ob.dob}\nNumber of Course assign : {len(ob.course)}""")
            for _ in range(len(ob.course)):
                print(f"Marks of {ob.course[_][0]} :", ob.course[_][1])
            print("------------------------------------")
         
    def search_by_course(self, course_name): 
        
        course_manage = []
        
        for i in range(ls.__len__()):
            if course_name in ls[i].course[0][0]:
                course_manage.append(ls[i].name)
    
        print(f"Number of student assign {course_name} : ",len(course_manage))
        print("Name :",", ".join(str(x) for x in course_manage))
  
    def delete(self, name):
        for i in range(ls.__len__()):
            if name in ls[i].name:
                print(f"Student name: {name} will be kick out")
                del ls[i]



obj = Student('' ,'', '' ,  0)
obj.add('Aiden', 'bi10-124', '2001', (('Advanced Programming ','17'),('French ','15')) )
obj.add('Na', 'bi10-010', '2001', (('Advanced Programming','16'),('Chemistry','12')) )
obj.add('Mr.Killer', '????', '', (('Kamikaze','19'),('Throwing knife','18')) )

for i in range(len(ls)):
    obj.display(ls[i])
    
obj.search_by_course('Advanced Programming')

obj.delete('Mr.Killer')