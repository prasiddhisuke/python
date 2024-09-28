class MyClass:
    def Get_String(self):
        self.MyStr=input("enter any string:")
    def print_String(self):
              s=self.MyStr
              print("string in Upper Case:",s.upper())
obj=MyClass()
obj.Get_String()
obj.print_String()              