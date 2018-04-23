# PythonForProgrammers/SimpleClass.py
class Simple:
    def __init__(self, str):
        print("Inside the Simple constructor")
        self.s = str

    # Two methods:
    def show(self):
        print(self.s)

    def showMsg(self, msg):
        # Calling another method
        print(msg + ':', self.show())


"""When the Python interpreter reads a source file, 
it executes all of the code found in it.
Before executing the code, it will define a few special variables. 
For example, if the python interpreter is running that module 
(the source file) as the main program, it sets the special 
__name__ variable to have a value "__main__". 
If this file is being imported from another module, 
__name__ will be set to the module's name.
"""
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    # Create an object:
    x = Simple("constructor argument")
    x.show()
    x.showMsg("A message")
