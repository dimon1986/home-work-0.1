import random


def riddle(digit=100, attempt=5):
    """можно отправить в функцию другие значения и будет сложнее или легче"""
    attempt = attempt
    digit = random.randrange(digit)
    print('Вы слышите мерзкий голос, который говорит: \n'
          f'жалкий человечишко, у тебя {attempt} попыток одгадать число,\n'
          'если они кончатся ты будешь погибать. Ха ха ха!!\n')
    answer = None

    while digit != answer:
        try:
            answer = int(input('Так что за число загадал, мой Внеземной Разум?'))
            if answer < digit:
                print(f'Ты ошибся значение больше!!')
            elif answer > digit:
                print(f'Смертный значение мешьше.')
            attempt -= 1
            if attempt == 0:
                print('Та ты не постиг мой Разум, но ничего теперь постигнишь ВЕЧНОСТЬ!\n'
                      f'А цифра была номер: {digit}')
                break
        except ValueError:
            print('Хорошо будем читать, что я этого не услышал, повторим вопрос.')
        else:
            if answer == digit:
                print('\n\nТебе повезло кожаный мешок,\n'
                      'Я сдержу слово и верну тебя на землю.\n'
                      f'Как ты угадал это было {digit}?')

riddle()
input('\n\nНажмите Enter, что бы выйти...')
