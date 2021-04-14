import zipfile


from Manage_Input import Input_Manage
from Manage_Output import Output_Manage

class domains:
    def __init__(self):
        pass


    def ex5(self,):

        obj = Input_Manage('' ,'', '' ,  0)
        obj.add('Aiden', 'bi10-124', '2001', (('Advanced Programming ','17.5'),('French ','15.25'), ('Singal ','14.25'), ('Basic Database','17.25')) )
        obj.add('Na', 'bi10-010', '2001', (('Advanced Programming','16.75'),('Chemistry','12.25'), ('Web Dev', '19')) )

        obj.export(obj.students_list)
        obj.running()

if __name__ == "__main__":
    main = domains() 
    main.ex4()