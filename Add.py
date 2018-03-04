a = 1
b = 2
print 'a+b=',a+b

class Add():
  def __init__(self):
    pass
  
  def add(self, var1, var2):
    return var1+var2

aclass = Add()
print '1+2=',aclass.add(1,2)
