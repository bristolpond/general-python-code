a = 1
b = 2
print 'a+b=',a+b

class Add():
  def __init__(self):
    pass
  
  def add(self, var1, var2):
    return var1+var2

class Add3(Add):
  def add3(self, var1, var2, var3):
    return var1+var2+var3
  
aclass = Add()
print '1+2=',aclass.add(1,2)
anclass = Add3()
print '1+2',anclass.add(1,2)
