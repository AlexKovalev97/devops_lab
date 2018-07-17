import __future__
import re


def checker(exp):
    pattern = r'-?(\d*)(\+|\-|\*|\/)*(\d*)\=-?(\d*)'
    m = re.match(pattern, exp)
    if m is not None:
        length = len(exp)
        amount_of_eq = exp.count('=')
        amount_of_spaces = exp.count(' ')
        amount_of_dots = exp.count('.')
        if amount_of_eq == 1 and amount_of_spaces == 0 and amount_of_dots == 0\
                and length < 100:
            eq_pos = exp.find('=')
            before_eq = exp[:eq_pos]
            after_eq = exp[eq_pos + 1:]
            try:
                result = eval(compile(before_eq, '<string>', 'eval',
                                      __future__.division.compiler_flag))
                if float(result) == float(after_eq):
                    print("YES")
                else:
                    print("NO")
            except ValueError:
                print("ERROR")
            except ZeroDivisionError:
                if float(after_eq) != 0:
                    print("NO")
                else:
                    print("YES")
            except SyntaxError:
                print("ERROR")
        else:
            print("ERROR")
    else:
        print("ERROR")


if __name__ == '__main__':
    exp = str(input('Input your expression: '))
    checker(exp)
