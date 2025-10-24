class student:
    def __del__(self):
        print("destructor called,object deleted")
        s=student()#object created
        del s #destructor called immediately
