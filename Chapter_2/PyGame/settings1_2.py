import pygame
from pygame.sprite import Sprite


class Settings(object):
    """Обычный калсс для хранения размеров экрана"""
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 490
        self.bg_color = (110, 90, 125)


class InputBox(Sprite):
    """Класс для ввода названия блюд,
    наследуемся от спрайта и передаем ему экран, текст, что-это,
    значение х, у, ширину, высоту"""
    def __init__(self, screen, txt='', the='',
                 x=10, y=10, width=300, height=50):
        super(InputBox, self).__init__()
        # можно создать мета класс, в него засунуть экран, цвета,
        # чуток текста и активность
        self.screen = screen
        self.rect_scr = screen.get_rect()
        self.COLOR_INACTIVE = (245, 115, 130)
        self.COLOR_ACTIVE = (250, 250, 250)
        self.color = self.COLOR_INACTIVE
        self.active = False
        self.backspace = False
        self.the = the
        self.font = pygame.font.SysFont(None, 32)
        self.txt = txt
        self.txt_rect = self.font.render(txt, True, (250, 250, 250))
        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        """обновляем текст по середини и в лево, когда пишем
        и отрисовываем прямоугольную область"""
        self.screen.blit(self.txt_rect, (self.rect.left + 5, self.rect.top + 15))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)

    def draw(self):
        """если что уменьшаем длину и всегда обновляем"""
        if len(self.txt) > 16:
            self.txt = self.txt[:-1]
            self.update()
        self.update()


class Label(Sprite):
    """Просто надпись"""
    def __init__(self, screen, txt='', the='',
                 x=10, y=120, width=620, height=50):
        super(Label, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = (245, 115, 130)
        # говорм чей лейбл, что бы одна и таже функция работала
        self.the = the
        self.font = pygame.font.SysFont(None, 32)
        self.txt = txt
        # рендерим получиный текст
        self.txt_rect = self.font.render(txt, True, (250, 250, 250))
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        # self.screen.fill((190, 110, 130), self.rect)
        # можно добавить цвет фона и рамку, отрисовываем текст
        self.screen.blit(self.txt_rect, (self.rect.left + 5, self.rect.top + 15))
        # pygame.draw.rect(self.screen, self.color, self.rect, 2)


class Button(Sprite):
    """Класс кнопки, 
    наверно как-то более красиво можно сделать."""
    def __init__(self, screen, txt,  x=0, y=35,
                 width=0, height=50):
        super(Button, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.COLOR_BUTTON = (250, 180, 150)  # основной цвет кнопки
        self.HOVER_BUTTON = (50, 95, 125)  # цвет:hover кнопки
        self.txt_color = (255, 255, 255)  # основной цвет текста
        self.font = pygame.font.SysFont(None, 32)  # Размер и шрифт
        # флаг для переключения состояния кнопки
        self.hover = False
        # Построение объекта rect кнопки и выравнивание где нам нада.
        self.rect = pygame.Rect(x, y, width, height)
        # Сообщение кнопки создается только один раз.
        self.prep_msg(txt)

    def prep_msg(self, txt):
        """Преобразует msg в прямоугольник и выравнивает текст по центру.
        просто прямоуголник с цветом и текстом-картинкой"""
        self.txt = txt  # нужна для определения, хранит стринг
        # рендерим текст
        self.txt_image = self.font.render(txt, True, self.txt_color)
        # создаем прямоугольник текста и его центр становиться центром кнопки
        self.txt_rect = self.txt_image.get_rect()
        self.txt_rect.center = self.rect.center

    def update(self):
        # меняем цвет кавадрата вокруг кнопки
        self.screen.fill(self.HOVER_BUTTON, self.rect)
        self.screen.blit(self.txt_image, self.txt_rect)
        pygame.draw.rect(self.screen, (245, 115, 130), self.rect, 2)  # последний аргумент ширина border!

    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения поверх неё.
        self.screen.fill(self.COLOR_BUTTON, self.rect)
        self.screen.blit(self.txt_image, self.txt_rect)
        pygame.draw.rect(self.screen, (245, 115, 130), self.rect, 2)