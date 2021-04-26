class Input_Manage:
    
    def __init__(self, name, sid, dob, course):
        self.name   = name
        self.sid    = sid
        self.dob    = dob
        self.course = course
        self.students_list = []
    
    def add(self, name, sid, dob, course ):
        ob = Input_Manage(name, sid, dob, course)
        self.students_list.append(ob)
        
    def pickle_compress(self, filename):

        with open(filename, 'r') as file:
            data = file.read().replace('\n', '')

        dbfile = open(filename+'.pkl', 'ab')
      
        pickle.dump(data, dbfile)
        
    def pickle_decompress(self,filename):
        f = open(filename,'r')
        data = pickle.load(f)

        print(data)
        f.close()
        
        
    def export(self,infos):
        for content in infos:
            with open('students.txt','a+') as f:
                f.write('Name :'+content.name+'\n')
                f.write('  Student-ID: '+content.sid+'\n')
                f.write('  Date Of Birth'+content.dob+'\n')
                
            with open('courses.txt','a+') as f1:
                f1.write('Name :'+content.name+'\n')
                for _ in content.course:
                    f1.write('  Course:'+_[0]+'\n')
                
            with open('marks.txt','a+') as f2:
                f2.write('Name :'+content.name+'\n')
                for _ in content.course:
                    f2.write(f'  {_[0]}:'+_[1]+'\n')
                   