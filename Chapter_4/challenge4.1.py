print('Дорогой друг я могу посчитать для тебя столько сколько захочешь.')


def deem_run(start=0, end=10, step=1,):
    """по сути просто range только с интерактивностью"""
    while True:
        try:
            start = int(input('\nВведи начальную цифру со скольки начинать считать:'))
            end = int(input('\nВведи конечную цифру до куда считать(не включительно):'))
            step = int(input('\nМожно ввести интервал счёта:'))
        # если не то ввели
        except ValueError:
            print('введи целочисленное значение!')

        if end < start:
            step = - step
        for i in range(start, end, step):
            print(i, end=' ')
        ext = input('\n\nВведите символ, для прирывания счёта - иначе Enter.')
        if ext:
            break

deem_run()
input('\n\nНажмите Enter, что бы выйти...')