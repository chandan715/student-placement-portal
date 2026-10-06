class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        res1=self.a+self.b
        return res1
    def sub(self):
        res2=self.b-self.a
        return res2
    def mul(self):
        res3=self.a*self.b
        return res3
    def div(self):
        res4=self.a/self.b
        return res4
a=int(input())
b=int(input())
obj=Calculator(a,b)
print(obj.addition())
print(obj.sub())
print(obj.mul())
print(obj.div())