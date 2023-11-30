def fns() :
    text = input('Введите строку: ')
    register : dict[str, int] = {}
    for a in text:
        if a.isalpha() and a not in register:
         register[a] = 1
        elif a.isalpha() and a in register :
            register[a] += 1
        
    print('C учетом регистра')
    for a, count in register.items():  
       print('Буква -' ,a, 'повторилась' ,count, 'раз/a')
if __name__=='__main__':
    fns()