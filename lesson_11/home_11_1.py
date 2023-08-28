import random

words = open('words.txt', 'r')
words_list = words.read()
split_words_list = words_list.split(',')

def check_password():
    two_words = random.sample(split_words_list, 2)
    first_word = two_words[0]
    second_word = two_words[1]
    words_password = first_word + second_word
    try:  
        if len(first_word) < 3 or len(second_word) < 3:
            raise Exception(f'{words_password} Ошибка,одно из слов меньше 3 букв')
        if len(words_password) < 8 or len(words_password) > 10:
            raise ValueError(f'{words_password} Ошибка, неверная длина пароля')
    except Exception as rm:
        print(rm)
    except ValueError as mvr:
        print(mvr)
    else:
        print(f'Ваш пароль: {words_password}')
    finally:
        words.close()
        


if __name__ =='__main__':
    check_password()

