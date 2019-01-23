import sys
import pygame
import random


def event_choice(gui):
    """находим нужный элемент по линк, рондом и вставляем картинку"""
    for elm in gui.sprites():
        if elm.link == '1':
            digit = random.randint(1,5)
            # .convert_alpha() для быстрой загрузки
            image = pygame.image.load(f"{elm.dict_images[digit]}").convert_alpha()
            # трансформируем её, что бы она была крупнее
            elm.area = pygame.transform.scale(image, (100, 100))


def event_flip(gui):
    def flip_coin(cast):
        """подбрасываем монетку"""
        try:
            cast = int(cast)  # считываем значение
            heads = 0  # орел
            tails = 0  # решка
            while cast != 0:  # можно и range, но профит?
                luck = random.randint(0, 1)  # рандомим удачу, есть или нет
                if luck == 1:
                    heads += 1
                else:
                    tails += 1
                cast -= 1  # отнимаем каст, до тех пор пока он не станет равен 0, тогда прирываем цыкл
            for elm in gui.sprites():
                # находим коин и вписываем тхх в него
                if elm.the == 'coin':
                    elm.txt = (f"Орёл выпал {heads}, решко выпало {tails}")
        except ValueError:
            for elm in gui.sprites():
                # так же находим, выводим предупреждение
                if elm.the == 'coin':
                    elm.txt = (f"Введите значение, не пиши чушь!")

    for elm in gui.sprites():
        # если инпут значение сколько бросков отправляем дальше
        if elm.the == 'input':
            flip_coin(elm.txt)
        # по линку находим нужную картинку и делаем её активной
        if elm.link == '2':
            elm.active = True


def pos_button(gui, mouse_x, mouse_y):
    """Проверяет находиться ли мышка над элементом
    и изменяет флаг"""
    for elm in gui.sprites():  # для каждой кнопки входяший в гуи
        button_pos = elm.rect.collidepoint(mouse_x, mouse_y)  # проверка на наличие коллизий(есть или нет 1:0)
        if button_pos:
            elm.hover = True  # если мышка над элементом то флаг переключается на тру
        else:
            elm.hover = False  # иначе флаг переключается на фолс


def check_gui(gui, mouse_x, mouse_y):
    """если колизия есть и она не с картинкой, то актив Тру,
    цвет, фон, обводка меняются, если нет, то фолс, если фолс когда идёт вращение,
    возвращаем картинки к начальному отображению, кулдаун сбрасываем.
    """
    for elm in gui.sprites():
        if elm.rect.collidepoint(mouse_x, mouse_y) and elm.the != 'img':
            elm.active = True
        else:
            elm.active = False
            if elm.the == 'img':
                image = pygame.image.load(f"{elm.dict_images[0]}").convert_alpha()
                elm.area = pygame.transform.scale(image, (100, 100))
                elm.cooldown = 0
    # НАМ НУЖНО ЧТО БЫ СНАЧАЛА ТРУ ПОЯВИЛОСЬ У ИНТЕРЕСУЮЩЕГО НАС ОБЪЕКТА
    # ТАК КАК ЕСЛИ ОН ТРУ ТО СРАБАТЫВАЕТ ДРУГОЙ ОБЪЕКТ ^_^
    for elm in gui.sprites():
        # проверка нажали ли на кнопку, если да, то узнаем что на ней написанно и отправляем gui дальше
        button_clicked = elm.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            if elm.txt == 'Рондом':
                event_choice(gui)
            elif elm.txt == 'Подбросить монетку':
                event_flip(gui)


def key_down_events(gui, event):
    """всё как обычно нажал кнопку, получи гранату,
    проверка на инпут, включаем бекспейс или записываем текст"""
    if event.key == pygame.K_ESCAPE:
        # ескейп и выходим
        sys.exit()
    if event.type == pygame.KEYDOWN:
        for elm in gui.sprites():
            # если активин элемент и он является инпутом
            if elm.active and elm.the == 'input':
                # если кей бэкспейс,то флаг Тру
                if event.key == pygame.K_BACKSPACE:
                    elm.backspace = True
                else:
                    # инече добовляем текст юникода а тхт
                    elm.txt += event.unicode
                # отрисовываем тхт
                elm.draw_txt()


def check_event(gui):
    """события: выхода, мышка над элементом, нажатие на мышку,
    нажатие на клавиши, подъём бэкспйса"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # просто два инта
            pos_button(gui, mouse_x, mouse_y)  # для функции
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_gui(gui, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            key_down_events(gui, event)
        elif event.type == pygame.KEYUP:
            for elm in gui.sprites():
                if elm.the == 'input':
                    if event.key == pygame.K_BACKSPACE:
                        # меняем его на лож, что бы не удалялось
                        elm.backspace = False


def update_screen(stg, screen, gui):
    # вставляем бэкграунд
    screen.fill(stg.bg_color)
    for elm in gui.sprites():
        # если НЕ ховер, то рисуем
        if not elm.hover:
            elm.draw()
        # если над кнопкой мышка, то по особенному отрисовывается
        if elm.hover:
            elm.update_is_hover()
        # если активен(нажат) виджет, то по особому отрисовывается
        if elm.active:
            elm.update_is_active()
        # если инпут с активным бэкспейсом, то удаляем последней элемент
        if elm.the == 'input':
            if elm.backspace:
                # удаяем последний элемент, если бэкспйс есть
                elm.txt = elm.txt[:-1]
        # просто если картинка, то тоже собственый метод отрисовки
        if elm.the == 'img':
            elm.draw_img()
    pygame.display.flip()