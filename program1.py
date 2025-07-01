class Calculator:
  def __init__(self,a:float ,b:float ,operation:str ):
      self.a=a
      self.b=b
      self.operation=operation
  def calculation(self):
    if self.operation=='+':
      return self.a+self.b
    elif self.operation=='-':
      return self.a-self.b 
    elif self.operation=='*':
      return self.a*self.b 
    elif self.operation=='/' and b!=0:
      return self.a/self.b   
    elif self.operation=='//' and b!=0:
      return self.a//self.b
    else:
      raise ValueError('Zero division error')
a=float(input('enter the value of a:')) 
b=float(input('enter the value of b:'))
operation=input('enter operation:')    
cal=Calculator(a,b,operation)
try:
    result=cal.calculation()
    print(f"The result of {a} {operation} {b} is:{result}")
except ValueError as e:
    print('error:',e)
