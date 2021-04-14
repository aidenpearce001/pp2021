class Output_Manage:
    def __init__(self, students_list):
        self.students_list = students_list
    
    def display(self,students_list):
        for info in students_list:
            print(f"""Name : {info.name}\nStudent ID : {info.sid}\nDate Of Birth : {info.dob}\nNumber of Course assign : {len(info.course)}""")
            for _ in range(len(info.course)):
                print(f"Marks of {info.course[_][0]} :", info.course[_][1])
            print("------------------------------------")    
            