def home(text):
    symbols = []
    for i in text:
        if i == '(' or i == '{' or i == '[':
            symbols.append(i)
        elif len(symbols) != 0:
            if symbols[0] == '{' and i == '}' or symbols[0] == '(' and i == ')' or symbols[0] == '[' and i == ']':
                if len(symbols) == 0:
                    print('False')
                else:
                    symbols.pop()
        else:
            if len(symbols) >= 1:
                symbols.pop()
            else:
                print('False')
                exit()
    if len(symbols) == 0:
        print('True')
    else:
        print('False')


# print(home("()"))  # True
# print(home("()[]{}"))  # True
# print(home("(]"))  # False


home(input('Введите любую последовательность скобок: '))