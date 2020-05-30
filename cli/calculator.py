def is_number(number):
    try:
        float(number)
    except ValueError:
        return False
    return True

def precedence(op):
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0


class CalculatorV01:
    
    @classmethod
    def enter(cls,operation):
        try:
            result = cls.calculate(operation)
        except (ZeroDivisionError,TypeError):
            result = 'Enter a valid operation!'
        return result

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

    @classmethod
    def calculate(cls,operation):
        if is_number(operation):
            if operation.isdigit():
                return int(operation)
            return float(operation)

        data_operators = {
            '+': cls.add,
            '-': cls.sub,
            '*': cls.mul,
            '/': cls.div
        }
        for op in data_operators:
            left_number,operator,right_number = operation.partition(op)
            if operator in data_operators:
                return data_operators[operator](cls.calculate(left_number),cls.calculate(right_number))
        raise TypeError


class CalculatorV02:

    @classmethod
    def enter(cls,operation):
        try:
            result = cls.calculate(operation)
        except:
            result = 'Error'
        return result        

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

    
    @classmethod
    def calculate(cls,operation):

        op_mapping = {
            '+': cls.add,
            '-': cls.sub,
            '*': cls.mul,
            '/': cls.div
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