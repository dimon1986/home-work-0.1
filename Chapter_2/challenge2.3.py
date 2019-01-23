
def car_dealer(agency_fee=1000, delivery=500):
    # всё обернул в функцию, если что агенский увеличить и доставку
    while True:
        try:
            # сумма за машину
            invoice = int(input('Сколько будет стоить ваша машина?'))
            if invoice:
                tax = invoice * 0.13
                charge = invoice * 0.2
                # все добавленные наценки
                print(f'Автодиллир говорит:\n'
                      f'Все расчёты на сумму {invoice}, \n'
                      f'Так обычные 13% это будет плюс: {tax} \n'
                      f'Регистрационный сбор 20% плюс: {charge} \n'
                      f'Агентский сбор {agency_fee} рублей и доставка {delivery} рублей\n'
                      f'Итого: {invoice+tax+charge+agency_fee+delivery}')
                break
        except ValueError:
            print('что-то твои кривые пальци не то набрали, поэтому попробуем повторить.')

car_dealer()

print('\n\nЕсли не очень точные цыфры, то познакомтитьсь, они вещественные.')
input('\n\nНажмите Enter, что бы выйти...')