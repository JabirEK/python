class PyCharm:
    def execute(self):
        print("compliling")
        print("Running")

class MyEditor:
    def execute(self):
        print("spell check")
        print("compliling")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute()
        print("Done")

# ide = MyEditor()

ide = PyCharm()

lap = Laptop()
lap.code(ide)