from tkinter import *


def precedence(op):
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0



class Calculator:

    result = False
    expression='0'
    op = ['+','-','÷','x','%']

    @classmethod
    def clear(cls,display):
        cls.expression='0'
        display.set(cls.expression)       

    @classmethod
    def press(cls,num_op,display):

        if (cls.expression == '0' or cls.result) and num_op.isdigit():
            cls.expression = num_op
        elif cls.expression[-1] in cls.op and num_op in cls.op:
            cls.expression = cls.expression[:-1]
            cls.expression+=num_op
        else:
            cls.expression+=num_op

        display.set(cls.expression)
        cls.result=False

    @classmethod
    def press_bracket(cls,bracket,display):
        if cls.expression == '0' and bracket =='(' :
            cls.expression = bracket
        elif bracket ==')':
            if cls.expression.count('(')>cls.expression.count(bracket) and (cls.expression[-1].isdigit() or cls.expression[-1]==')'):
                cls.expression+=bracket
        else:
            if cls.expression[-1] in cls.op or cls.expression[-1]=='(':
                cls.expression+=bracket
        display.set(cls.expression) 

    @classmethod
    def equal(cls,display):
        if cls.expression.count('(') == cls.expression.count(')') and cls.expression[-1] not in cls.op:
            cls.expression = str(cls.calculate(cls.expression))
            cls.result = True
        
        display.set(cls.expression)


    @staticmethod
    def add(number1,number2):
        return number1+number2 

    @staticmethod
    def sub(number1,number2):
        return number1-number2

    @staticmethod
    def div(number1,number2):
        return number1/number2

    @staticmethod
    def mul(number1,number2):
        return number1*number2

    @staticmethod
    def percent(number1,number2):
        return (number1/100)*number2

    
    @classmethod
    def calculate(cls,operation):

        op_mapping = {
            '+': cls.add,
            '-': cls.sub,
            'x': cls.mul,
            '%': cls.percent,
            '÷': cls.div
        }

        stack_op = []
        stack_val = []

        i = 0
        while i < len(operation):
            if operation[i] == ' ':
                i+=1
                continue
            
            if operation[i].isdigit() or operation[i] == '.':
                value = 0
                decimal = 0
                base_10 = 1
                if operation[i].isdigit():
                    while i<len(operation) and operation[i].isdigit():
                        value = (value * 10) + int(operation[i])
                        i+=1
                    if i<len(operation) and operation[i] == '.':
                        i+=1
                        while i<len(operation) and operation[i].isdigit():
                            base_10*=10
                            decimal= (decimal*10)+int(operation[i])
                            i+=1
                else:
                    i+=1
                    while i<len(operation) and operation[i].isdigit():
                        base_10*=10
                        decimal= (decimal*10)+int(operation[i])
                        i+=1
                decimal/=base_10
                value+=decimal
                stack_val.append(value)
                continue

            if operation[i] == '(':
                stack_op.append(operation[i])
            elif operation[i] == ')':
                if stack_op[-1]=='(':
                    stack_op.pop()
                else:
                    value1 = stack_val.pop()
                    value2 = stack_val.pop()
                    op = stack_op.pop()

                    stack_val.append(op_mapping[op](value1,value2))
                    stack_op.pop()
                
            else:
                while len(stack_op)!=0 and precedence(stack_op[-1])>=precedence(operation[i]):
                    value2 = stack_val.pop()
                    value1 = stack_val.pop()
                    op = stack_op.pop()

                    stack_val.append(op_mapping[op](value1,value2))
                stack_op.append(operation[i])

            i+=1
        
      
        while len(stack_op)!=0:
            value2 = stack_val.pop()
            value1 = stack_val.pop()
            op = stack_op.pop()

            stack_val.append(op_mapping[op](value1,value2))
        return stack_val[-1]

class Window(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.init_window()

    def create_buttons(self,display):
        mapping =[
            ('CLE','Orange',lambda:Calculator.clear(display)),
            ('(','Gray',lambda:Calculator.press_bracket('(',display)),
            (')','Gray',lambda:Calculator.press_bracket(')',display)),
            ('%','Gray',lambda:Calculator.press('%',display)),
            ('7','LightBlue',lambda:Calculator.press('7',display)),
            ('8','LightBlue',lambda:Calculator.press('8',display)),
            ('9','LightBlue',lambda:Calculator.press('9',display)),
            ('x','Gray',lambda:Calculator.press('x',display)),
            ('4','LightBlue',lambda:Calculator.press('4',display)),
            ('5','LightBlue',lambda:Calculator.press('5',display)),
            ('6','LightBlue',lambda:Calculator.press('6',display)),
            ('÷','Gray',lambda:Calculator.press('÷',display)),
            ('1','LightBlue',lambda:Calculator.press('1',display)),
            ('2','LightBlue',lambda:Calculator.press('2',display)),
            ('3','LightBlue',lambda:Calculator.press('3',display)),
            ('-','Gray',lambda:Calculator.press('-',display)),
            ('0','LightBlue',lambda:Calculator.press('0',display)),
            ('.','LightBlue',lambda:Calculator.press('.',display)),
            ('=','LightGreen',lambda:Calculator.equal(display)),
            ('+','Gray',lambda:Calculator.press('+',display))
        ]
        self.buttons = []
        for i,(name,color,event) in enumerate(mapping):
            self.buttons.append(
                Button(self,text=name,width=13,height=5,bg=color,command=event)
            )
            row,column = divmod(i,4)

            self.buttons[i].grid(row=row+1,column=column,padx=3,pady=3)

    def init_window(self):

        self.master.title('Calculator Python3')
        self.config(bg='black',padx=3,pady=3)
        self.grid()

        display = StringVar(value='0')
        entry = Entry(self,width = 38, font = ('Arial','20'),justify=RIGHT,bd=10,state='disabled',disabledbackground='white',disabledforeground='black',textvariable=display)
        entry.grid(columnspan=4,pady=3,padx=3)

        self.create_buttons(display)
