class Calc():
    def set_number(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def plus(self):
        try:
            if isinstance(self.num1,int) and isinstance(self.num2,int):
                return self.num1 + self.num2
            else:
                raise
        except:
            print('숫자만 입력 가능합니다. plus')
        
    
    def minus(self):
        try:
            return self.num1 - self.num2
        except:
            print('숫자만 입력 가능합니다. misun')    
    
    def multiple(self):
        try:
            if isinstance(self.num1,int) and isinstance(self.num2,int):
                return self.num1 * self.num2
            else:
                raise
        except:
            print('숫자만 입력 가능합니다. multiple')    
    
    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print('0으로 나눌 수 없습니다.')
        except:
            print('숫자만 입력 가능합니다. div')    
        

calc = Calc()

calc.set_number(20,10)

print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide())