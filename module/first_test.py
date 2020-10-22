

def spam(number):

    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    return "bulochka"*number


def my_sum(list_of_numbers):
    res = 0
    for x in list_of_numbers:
        res += x
    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    
    """
    return "res
    #  ...wite your code here


def shortener(string):
   

    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    return " ".join([x[:6]+"*" if len(x) > 6 else x for x in string.split()])
    #  ...wite your code here


def compare_ends(words):
    res = 0
    for string in words:
        if len(string) >= 2 and string[0] == string[-1]:
            res += 1
        else:
            pass

    #Функция получает на вход массив строк. Вернуть надо количество строк,
    #которые не короче двух символов и у которых первый и последний
    #символ совпадают.

    return res
    #  ...wite your code here

