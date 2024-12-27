#Create class employee
class Employee:
    #initialize the constructor
    def __init__(self):
        print("Employee created")
    #deconstructor
    def __del__(self):
        print("Employee deleted")
#create an object to call the class
obj = Employee()#executes the employee class
del obj #deletes theobject and calls the deconstructor