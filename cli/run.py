import sys
from calculator import CalculatorV01,CalculatorV02

def run():
    if sys.argv[-1] == 'brackets':
        print('--------------- Welcome to the Python3 Calculator With Brackets ---------------')
        calc = CalculatorV02
    else:
        print('--------------- Welcome to the Python3 Calculator No Brackets ---------------')
        calc = CalculatorV01
    print('To exit the program: exit')
    print()
    while True:
        print('Enter: ', end='')
        operation = input()
        if operation == 'exit':
            print('Closing the program...')
            return
        
        print('Answer: {}'.format(calc.enter(operation)))
        print()



if __name__ == '__main__':
    run()