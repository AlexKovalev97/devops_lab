import __future__
import re
expression = str(input('Input your expression: '))
pattern = r'-?(\d*)(\+|\-|\*|\/)*(\d*)\=-?(\d*)'
m = re.match(pattern, expression)
if m is not None:
    length = len(expression)
    amountOfEq = expression.count('=')
    amountOfSpaces = expression.count(' ')
    amountOfDots = expression.count('.')
    if amountOfEq == 1 and amountOfSpaces == 0 and amountOfDots == 0\
            and length < 100:
        eqPos = expression.find('=')
        beforeEq = expression[:eqPos]
        afterEq = expression[eqPos + 1:]
        try:
            result = eval(compile(beforeEq, '<string>', 'eval',
                                  __future__.division.compiler_flag))
            if float(result) == float(afterEq):
                print("YES")
            else:
                print("NO")
        except ValueError:
            print("ERROR")
        except ZeroDivisionError:
            if float(afterEq) != 0:
                print("NO")
            else:
                print("YES")
        except SyntaxError:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")
