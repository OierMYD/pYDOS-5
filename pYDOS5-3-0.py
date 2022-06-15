from random import*
from time import*
import os
logo = """
|-----------------------------------|
|            Pythonix               |
|             pY-DOS                |
|           Version 5.3             |
|-----------------------------------|
"""
def dos():
    print(logo)
    os.system("cls")
    sleep(2)
    while True:
        print("------------------------------------------------")
        print("Pythonix pY-DOS 5 Options Menu:>")
        space1 = "------------------------------------------------"
        print(space1)
        print("Settings:")
        space2 = "                                                "
        print(space2)
        print("1.About")
        print(space1)
        print("Apps & Docs:>")
        print(space2)
        print("2.Calculator.py")
        print("3.GuessingNumbers.py")
        print("4.Exit")
        print(space1)
        op = int(input("Local:>"))
        if op == 4:
            break
        elif op == 1:
            logodd = '''
            |----------|
            |
            |
            |----------|
                       |
                       |
            -----------|
            '''
            print(logodd)
            print("Pythonix pY-DOS 5.3.0 Standard ")
            print('Core:')
            print('Pythonix 1.0.3.0')
            pass
        elif op == 2:
            print("----------Calculator.py----------")
            print('Version 1.1')
            print("Choose a way:")
            print("1=+ 2=- 3=* 4=/")
            ways = int(input("Way:"))
            num1 = int(input("The first number is:"))
            num2 = int(input("The second number is:"))
            if ways == 1:
                print(num1 + num2)
            elif ways == 2:
                print(num1 - num2)
            elif ways == 3:
                print(num1 * num2)
            else:
                print(num1 / num2)
        elif op == 3:
            print("-----GuessingNumbers.py-----")
            print('Version 1.1')
            print("The number is from 1 to 100.")
            answer = randint(1,100)
            while 1:
                i = int(input("Guess:"))
                if i > answer:
                    print("It is big.")
                elif i < answer:
                    print("It is small.")
                else:
                    print("Great!")
                    sleep(0.5)
                    break
        else:
            print("Wrong letters.Type again.")
dos()    
