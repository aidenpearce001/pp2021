import pickle
import time
import threading

from Manage_Input import Input_Manage
from Manage_Output import Output_Manage

class domains(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(2)

        obj = Input_Manage('' ,'', '' ,  0)
        obj.add('Aiden', 'bi10-124', '2001', (('Advanced Programming ','17.5'),('French ','15.25'), ('Singal ','14.25'), ('Basic Database','17.25')) )
        obj.add('Na', 'bi10-010', '2001', (('Advanced Programming','16.75'),('Chemistry','12.25'), ('Web Dev', '19')) )

        pickled_object = pickle.dumps(obj)

        print(f"Object after pickled : { pickled_object }\n")

        unpickled_object = pickle.loads(pickled_object)
        print(f"One Student Name in Object after pickled: {unpickled_object.students_list[0].name}")

def timeout(total):

    time_left = total
    for i in range(total):
        print(f"Another Thread run end will end after {str(time_left)}s")
        time.sleep(1)
        time_left -=1
         
if __name__ == "__main__":
    print("Start testing Thread")
    t = domains()
    t1 = threading.Thread(target=timeout,args=(3,))

    t.start()
    t1.start()

    print("This line to show text after Thread Start")
    t.join()
    t1.join()

    print("DONE!!!")