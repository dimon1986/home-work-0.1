import os
import pygame
from pygame.sprite import Sprite


class Settings:
    """можно добавить функции которые будут менять сетинг"""
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (5, 40, 110)


class Widget(Sprite):
    """Родитель всех элементов
    интересно это имеится ввиду божественный объект или всё же норма,
    так как ведь основные моменты каждый сам за себя будут отвечать
    Атрибуты: screen - нужен для позиционирования и отображения
    the,link - ссылки к классу или ед.виджиту 
    font - это шрифт :) hover, active - флаги
    list_color - список для проверки на вхождение и его метод add_color
    Методы: prep_txt - создает рект текста и выравнивает его по центру
    update_is_hover - отрисовывает когда навели мышь bg, border, txt
    update_is_active - отрисовывает активный виджет bg, border, txt 
    draw - отрисовывает в спокойном состоянии bg, border, txt
    """
    COLOR = {'white': (255, 255, 255), 'black': (0, 0, 0,),
             'blue': (15, 65, 170), 'blue_dark': (40, 70, 130), 'blue_dark_1': (5, 40, 110),
             'blue_light': (15, 65, 170), 'blue_light_1': (110, 140, 215),
             'red': (240, 0, 40), 'red_dark': (180, 45, 65), 'red_dark_1': (150, 0, 25),
             'red_light': (250, 60, 90), 'red_light_1': (250, 110, 130),
             'yellow': (240, 250, 0), 'yellow_dark': (180, 190, 45), 'yellow_dark_1': (155, 165, 0),
             'yellow_light': (240, 250, 60), 'yellow_light_1': (245, 250, 115),
             'orange': (255, 170, 0), 'orange_dark': (190, 140, 50), 'orange_dark_1': (165, 110, 0),
             'orange_light': (255, 190, 65), 'orange_light_1': (255, 210, 115),
             }

    def __init__(self,
                 # экран, что это есть - если надо, текст,
                 screen, the=None, txt=None, link=None,
                 # цвета кнопки, текста, прямоугольника
                 bg_color=None, hover_bg_color=None, act_bg_color=None,
                 txt_color=None, hover_txt_color=None, act_txt_color=None,
                 border_color=None, hover_border_color=None, act_border_color=None,
                 # шрифт и его размер
                 font=None, size=10,
                 # x & y, размер бъекта
                 x=0, y=0, width=0, height=0, images=None):
        super(Widget, self).__init__()
        self.screen = screen
        self.the = the  # что бы обратиться к группе конкретных элементов
        self.link = link  # что бы всегда мог обратиться к конкретному элементу
        self.font = pygame.font.SysFont(font, size)  # Размер и шрифт
        # флаги для переключения состояния кнопки
        self.hover = False
        self.active = False
        self.list_color = []

        def add_color(k):
            # кривно конечно, но так проверяю нужно ли раскрашивать данный элемент
            self.list_color.append(k)
        # добавляем img если они None
        if images is not None:
            add_color('img')
        # если есть бекграунд, то ищим его в словаре, и добовляем
        if bg_color:
            self.bg_color = self.COLOR[bg_color]  # цвет: standard
            add_color('bg_color')
        if hover_bg_color:
            self.hover_bg_color = self.COLOR[hover_bg_color]  # цвет: hover
            add_color('hover_bg_color')
        if act_bg_color:
            self.act_bg_color = self.COLOR[act_bg_color]  # цвет: active
            add_color('act_bg_color')

        # если есть бордюр, то ищим его в словаре, и добовляем
        if border_color:
            self.border_color = self.COLOR[border_color]  # цвет: standard
            add_color('border_color')
        if hover_border_color:
            self.hover_border_color = self.COLOR[hover_border_color]  # цвет: hover
            add_color('hover_border_color')
        if act_border_color:
            self.act_border_color = self.COLOR[act_border_color]  # цвет: active
            add_color('act_border_color')

        # цвет текста во всех трёх случаях
        if txt_color:
            self.txt_color = self.COLOR[txt_color]  # цвет: standard
            add_color('txt_color')
        if hover_txt_color:
            self.hover_txt_color = self.COLOR[hover_txt_color]  # цвет: hover
            add_color('hover_txt_color')
        if act_txt_color:
            self.act_txt_color = self.COLOR[act_txt_color]  # цвет: active
            add_color('act_txt_color')

        # Построение объекта rect и выравнивание где нам нада.
        self.rect = pygame.Rect(x, y, width, height)
        # Сообщение кнопки создается только в том случае, если оно не является None
        if txt is not None:
            self.txt = txt
            self.prep_txt(txt)

    def prep_txt(self, txt):
        """Преобразует txt в прямоугольник и выравнивает текст по центру.
        просто прямоуголник с цветом и текстом-картинкой"""
        # рендерим текст
        self.area = self.font.render(txt, True, self.txt_color)
        # создаем прямоугольник текста и его центр становиться центром кнопки
        self.txt_rect = self.area.get_rect()
        self.txt_rect.center = self.rect.center
        if self.the == 'input':
            # для инпута центре поменяем, что бы начало начиналось слева
            self.txt_rect.center = (self.rect.left, self.rect.centery)

    def update_is_hover(self):
        # рисование прямоугольника, заливка цветом, блитинг текста.
        if 'hover_bg_color' in self.list_color:
            self.screen.fill(self.hover_bg_color, self.rect)
        if 'hover_border_color' in self.list_color:
            pygame.draw.rect(self.screen, self.hover_border_color, self.rect, 1)  # последний аргумент ширина rect!
        if 'hover_txt_color' in self.list_color and self.txt:
            self.txt_image = self.font.render(self.txt, True, self.hover_txt_color)
            self.screen.blit(self.txt_image, self.txt_rect)

    def update_is_active(self):
        # заливка цветом, рисование прямоугольника, блитинг текста.
        if 'act_bg_color' in self.list_color:
            self.screen.fill(self.act_bg_color, self.rect)
        if 'act_border_color' in self.list_color:
            pygame.draw.rect(self.screen, self.act_border_color, self.rect, 1)
        if 'act_txt_color' in self.list_color and self.txt:
            self.txt_image = self.font.render(self.txt, True, self.act_txt_color)
            self.screen.blit(self.txt_image, self.txt_rect)

    def draw(self):
        # заливка цветом, рисование прямоугольника, блитинг текста.
        if 'bg_color' in self.list_color:
            self.screen.fill(self.bg_color, self.rect)
        if 'border_color' in self.list_color:
            pygame.draw.rect(self.screen, self.border_color, self.rect, 1)
        if 'txt_color' in self.list_color and self.txt:
            self.txt_image = self.font.render(self.txt, True, self.txt_color)
            self.screen.blit(self.txt_image, self.txt_rect)


class Button(Widget):
    """Класс кнопки"""
    def __init__(self, screen, the='', txt='',
                 # цвета кнопки, текста, прямоугольника
                 bg_color='blue_light', hover_bg_color='blue_light_1', act_bg_color=None,
                 txt_color='white', hover_txt_color='yellow_light_1', act_txt_color='orange',
                 border_color='white', hover_border_color='white', act_border_color=None,
                 # шрифт и его размер
                 font='comicsansms', size=18,
                 # x & y, размер бъекта
                 x=0, y=310, width=200, height=50):
        # вот эта штука нифига не нравиться, интересно можно как нить сократить?
        super(Button, self).__init__(screen, the=the, txt=txt,
                                     # цвета кнопки, текста, прямоугольника
                                     bg_color=bg_color, hover_bg_color=hover_bg_color, act_bg_color=act_bg_color,
                                     txt_color=txt_color, hover_txt_color=hover_txt_color, act_txt_color=act_txt_color,
                                     border_color=border_color, hover_border_color=hover_border_color, act_border_color=act_border_color,
                                     # шрифт и его размер, x & y, размер бъекта
                                     font=font, size=size, x=x, y=y, width=width, height=height)


class Label(Widget):
    """Просто надпись
    с default - для сохранения изначального лейбла
    """
    def __init__(self, screen, the='', txt='',
                 # цвета лейбла, текста, прямоугольника
                 bg_color=None, hover_bg_color=None, act_bg_color=None,
                 txt_color='white', hover_txt_color='white', act_txt_color=None,
                 border_color=None, hover_border_color=None, act_border_color=None,
                 # шрифт и его размер
                 font='comicsansms', size=16,
                 # x & y, размер бъекта
                 x=10, y=15, width=100, height=50):
        # ну не нравиться мне это, может как через * распаковать?
        super(Label, self).__init__(screen, the=the, txt=txt,
                                    # цвета лейбла, текста, прямоугольника
                                    bg_color=bg_color, hover_bg_color=hover_bg_color,
                                    act_bg_color=act_bg_color,
                                    txt_color=txt_color, hover_txt_color=hover_txt_color,
                                    act_txt_color=act_txt_color,
                                    border_color=border_color, hover_border_color=hover_border_color,
                                    act_border_color=act_border_color,
                                    # шрифт и его размер, x & y, размер бъекта
                                    font=font, size=size, x=x, y=y, width=width, height=height)
        # дефаут - это начальное название лейбла, сейчас не надо, в будущем фиг знает.
        self.default = txt


class InputBox(Widget):
    """ИнпутБлок так же на основе элемента
    с draw_txt - удаляет лишнии символы и рэндерит текст"""
    def __init__(self, screen, the='input', txt='',
                 # цвета инпута, текста, прямоугольника
                 bg_color='white', hover_bg_color='white', act_bg_color='white',
                 txt_color='black', hover_txt_color='black', act_txt_color='black',
                 border_color='black', hover_border_color='black', act_border_color='yellow',
                 # шрифт и его размер
                 font='comicsansms', size=18,
                 # x & y, размер бъекта
                 x=0, y=277, width=50, height=30):
        super(InputBox, self).__init__(screen, the=the, txt=txt,
                                       # цвета инпута, текста, прямоугольника
                                       bg_color=bg_color, hover_bg_color=hover_bg_color, act_bg_color=act_bg_color,
                                       txt_color=txt_color, hover_txt_color=hover_txt_color, act_txt_color=act_txt_color,
                                       border_color=border_color, hover_border_color=hover_border_color, act_border_color=act_border_color,
                                       # шрифт и его размер, x & y, размер бъекта
                                       font=font, size=size, x=x, y=y, width=width, height=height)
        self.backspace = False

    def draw_txt(self, digit=3):
        if len(self.txt) > digit:
            self.txt = self.txt[:-1]
        if 'act_txt_color' in self.list_color and self.txt:
            self.txt_image = self.font.render(self.txt, True, self.act_txt_color)
            self.screen.blit(self.txt_image, (self.rect.left, self.rect.centery))


class Image(Widget):
    """Класс для картинки, 
    и словарь с сылками на изображения
    Атрибуты: индекс и кулдаун.
    Методы: gen_img- создаёт полные пути к картинкам
    enumeration - перелистывает картинки благодоря кулдауну и индексу
    draw_img - отрисовывает картинку, запускает перебор^"""
    def __init__(self, screen, the='img', txt='', link=None,
                 # цвета инпута, текста, прямоугольника
                 bg_color='white', hover_bg_color='white', act_bg_color='white',
                 txt_color='black', hover_txt_color='black', act_txt_color='black',
                 border_color='red', hover_border_color='red', act_border_color='red',
                 # шрифт и его размер
                 font='comicsansms', size=18,
                 # x & y, размер бъекта
                 x=75, y=75, width=200, height=200, images=None):
        super(Image, self).__init__(screen, the=the, txt=txt, link=link,
                                       # цвета инпута, текста, прямоугольника
                                       bg_color=bg_color, hover_bg_color=hover_bg_color, act_bg_color=act_bg_color,
                                       txt_color=txt_color, hover_txt_color=hover_txt_color, act_txt_color=act_txt_color,
                                       border_color=border_color, hover_border_color=hover_border_color, act_border_color=act_border_color,
                                       # шрифт и его размер, x & y, размер бъекта
                                       font=font, size=size, x=x, y=y, width=width, height=height, images=images)
        if images:
            # если есть картинки, создаётся словарь из картежов
            self.dict_images = dict(images)
            self.gen_img()
        self.index = 0
        self.cooldown = 0

    def gen_img(self):
        for k, v in self.dict_images.items():
            #  уточняю путь к картинке с помощью ос.паф передав ему подпапки
            self.dict_images[k] = os.path.abspath(v)
            # загрузка изображениий
            image = pygame.image.load(f"{self.dict_images[0]}").convert()
            # удаляю фон, черный
            image.set_colorkey((0, 0, 0))
            # укрупняю картинку
            self.area = pygame.transform.scale(image, (100, 100))
            # создаём рект изображения
            self.rect_image = self.area.get_rect()
            # центор изображения == ректу виджета(родителя)
            self.rect_image.center = self.rect.center

    def enumeration(self):
        """просто каждый раз загружаем новую картинку из словоря по индексу
        когда длина словоря равна картинкам обнуляем индекс и прибавляем кулдаун,
        после 3раз отключаем активность картинке и кулдаун на 0"""
        self.index += 1
        if self.index >= len(self.dict_images):
            self.index = 0
            self.cooldown += 1
            if self.cooldown >= 3:
                self.active = False
                self.cooldown = 0
        # если изображение содержит прозрачность (convert_alpha())
        img = pygame.image.load(f"{self.dict_images[self.index]}").convert_alpha()
        # трансформируем и он используется в отрисовке
        self.area = pygame.transform.scale(img, (100, 100))

    def draw_img(self):
        """рисует картинку в тикущей позиции"""
        if 'img' in self.list_color:
            self.screen.blit(self.area, self.rect_image)
        if self.active:
            self.enumeration()



