class Ap:
    def __init__(self,length,breath):
        self.breath=breath
        self.length=length
    def area(self):
        ar=self.length*self.breath
        return ar
    def para(self):
        pr=2*(self.length+self.breath)
        return pr
obj=Ap(20,10)
print(obj.area())
print(obj.para())