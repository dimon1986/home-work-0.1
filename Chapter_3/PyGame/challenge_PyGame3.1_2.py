from pygame.sprite import Group
from M_Dawson_Home_Work.Chapter_3.PyGame.settings1_2 import *
import M_Dawson_Home_Work.Chapter_3.PyGame.functions1_2 as f

# два кортежа с вложенными кортежами пнг картинок
images_weapons = ((0,'data//q.png'), (1,'data//weapons//1.png'),(2,'data//weapons//14.png'),
                  (3,'data//weapons//16.png'), (4,'data//weapons//21.png'),(5,'data//weapons//23.png'),)
images_many = ((0,'data//coin//1.png'),(1,'data//coin//2.png'),(2,'data//coin//3.png'),
               (3,'data//coin//4.png'),(4,'data//coin//5.png'),(5,'data//coin//6.png'),
               (6, 'data//coin//7.png'),(7,'data//coin//8.png'),(8,'data//coin//9.png'),)


def run_main():
    pygame.init()
    # клок это для кадров
    clock = pygame.time.Clock()
    # просто маленький класс, а так сюда можно кучу всего добавить(разрешения разные, фоны и т.д.)
    stg = Settings()
    pygame.display.set_caption('Пирожок & монетка')
    screen = pygame.display.set_mode((stg.screen_width, stg.screen_height))
    # создаём группу и объекты, азатем их добавляем в группу
    gui = Group()
    button = Button(screen, txt='Рондом', x=75)
    button1 = Button(screen, txt='Подбросить монетку', x=375)
    label = Label(screen,  txt='Сюрприз', x=125)
    label1 = Label(screen, txt='Монета', x=425)
    label2 = Label(screen, the='coin', txt='Значения орлов и решек!', x=420, y=380)
    input_box = InputBox(screen, x=450)
    image = Image(screen, link='1', images=images_weapons)
    image1 = Image(screen, link='2', x=375, images=images_many)
    gui.add(button, button1, label, label1, label2, input_box, image, image1)

    while True:
        # проверка событий
        f.check_event(gui)
        # обновление экрана
        f.update_screen(stg, screen, gui)
        # желаемое число кадров в секунду
        clock.tick(20)

if __name__ == '__main__':
    run_main()
