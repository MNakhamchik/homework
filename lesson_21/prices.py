def reshenie(data):
    first = '()'
    second = '[]'
    third = '{}'
    list = []
    for i in range(0, len(data),2):
        list.append(data[i:i+2])
    print(list)
    all_results = []
    for symbol in list:
        print(symbol)
        if symbol == first or symbol== second or symbol== third:
            all_results.append('True')
        else:
            all_results.append('False')
    print(all_results)
    false = 'False'
    if false in all_results:
        print(False)
    else:
        print(True)
data = "](["
reshenie(data)