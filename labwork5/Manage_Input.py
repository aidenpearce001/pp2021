class Input_Manage:
    def __init__(self, name, sid, dob, course, students_list=[]):
        self.name   = name
        self.sid    = sid
        self.dob    = dob
        self.course = course
        self.students_list = students_list
         
    def add(self, name, sid, dob, course ): 
        ob = Input_Manage(name, sid, dob, course)
        self.students_list.append(ob)
        
    def delete(self, name):
        for i in range(ls.__len__()):
            if name in ls[i].name:
                print(f"Student name: {name} will be kick out")
                del ls[i]