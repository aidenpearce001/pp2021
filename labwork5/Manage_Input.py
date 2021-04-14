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
        
    def file_compress(self, inp_file_names, output_name):

        compression = zipfile.ZIP_DEFLATED

        print(f' *** out_zip_file is - {output_name}')
        zf = zipfile.ZipFile(output_name, mode="w")

        try:
            for file_to_write in inp_file_names:
                print(f' *** Processing file {file_to_write}')
                zf.write(file_to_write, file_to_write, compress_type=compression)

        except FileNotFoundError as e:
            print(f' *** Exception occurred during zip process - {e}')

        zf.close()
        
    def compress(self):
        list_files = ['students.txt','courses.txt','marks.txt']
        
        self.file_compress(list_files, 'students.dat')
        
    def decompress(self):
        try:
            with zipfile.ZipFile("students.dat","r") as zip_ref:
                zip_ref.extractall("decompress")
        except Exeption as E:
            print('FILE students.dat not found')
            print('ERROR :',E)
        
        
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
                    
    def running(self):
        self.compress
        self.decompress