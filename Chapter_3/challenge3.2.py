import random

print('Сейчас я подкнину монету столько раз сколько звёзд на небе.')
while True:
    try:
        cast = int(input('Ладно шучу сколько раз надо подкинуть?'))
        heads = 0
        tails = 0
        while cast != 0:
            luck = random.randint(0, 1)
            if luck == 1:
                print('Выпал ОРЁЛ!')
                heads += 1
            elif luck == 0:
                print('Решко выпало.')
                tails += 1
            else:
                print('Да такого не бывает, если только монету не проглатил Великан.')
            cast -= 1
        print(f'Орёл выпал {heads}, решко выпало{tails}, за {heads+tails}шагов.')
        break
    except ValueError:
        print('Попробую ещё раз задать тебе вопрос.')
input('\n\nНажмите Enter, что бы выйти...')