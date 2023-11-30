def fns() :
    text = input('Введите строку: ')
    register_a: dict[str, int] = {}
    for a in text:
        if a.isalpha():
            a_upp = a.lower()
            if a_upp in register_a:
               register_a[a_upp] +=1         
            elif a_upp not in register_a :
               register_a[a_upp] = 1
    print('Без учета регистра')
    for a_upp, count in register_a.items():  
       print('Буква -' , a_upp, 'повторилась' ,count, 'раз/a')

if __name__=='__main__':
    fns()