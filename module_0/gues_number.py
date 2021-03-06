import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)
        if number == predict:
            return(count)
        
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count)


def game_core_v3(number):
    '''Процедура использует логарифмический подход для максимально быстрого нахождения значения.'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if predict <= number - 25:
            predict += 25
        elif predict >= number + 25:
            predict -= 25
        elif predict <= number - 12:
            predict += 12
        elif predict >= number + 12:
            predict -= 12
        elif predict <= number - 6:
            predict += 6
        elif predict >= number + 6:
            predict -= 6
        elif predict <= number - 3:
            predict += 3
        elif predict >= number + 3:
            predict -= 3
        elif predict > number:
            predict -= 1
        else:
            predict += 1
    return(count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за {} попыток".format(score))
    return(score)


score_game(game_core_v3)