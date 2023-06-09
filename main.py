from kivy.app import App
from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from random import randint as rand
from random import choice


PASSWORD = 'арина бомж слуга ильи'
RAD = 20
POOP = r'poop.png'
SCRIM = r'scrim.png'
FON = r'fon.png'
PRISON = r'prison.png'
FACES = [r'1face.png', r'2face.png', r'3face.png', r'4face.png']
r, g, b = 0, 0, 0


class Applick(App):
    """ГЛАВНЫЙ КЛАСС"""

    title = 'Приложение'

    def build(self):
        """строитель"""

        self.sm = ScreenManager()
        self.main_screen = MainScreen(name='main_screen')
        self.draw_screen = DrawScreen(name='draw_screen')
        self.points_screen = PointsScreen(name='points_screen')
        self.image_screen = ImageScreen(name='image_screen')
        self.camera_screen = CameraScreen(name='camera_screen')
        self.protected_screen = ProtectedScreen(name='protected_screen')

        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.draw_screen)
        self.sm.add_widget(self.points_screen)
        self.sm.add_widget(self.image_screen)
        self.sm.add_widget(self.camera_screen)
        self.sm.add_widget(self.protected_screen)

        return self.sm


class MainScreen(Screen):
    """ГЛАВНЫЙ ЭКРАН"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.fon_image = Image(source=FON, fit_mode='fill')
        self.main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.main_layout.btn_up = NavButton(nav='points_screen', size_hint=(.35, .5), text='Вверх')
        self.main_layout.layout = BoxLayout(orientation='horizontal', padding=8, spacing=8, size_hint=(1, .5))
        self.main_layout.layout.btn_left = NavButton(nav='draw_screen', text='Влево')
        self.main_layout.layout.btn_right = NavButton(nav='image_screen', text='Вправо')
        self.main_layout.layout.text = Label(text='Выбери')
        self.main_layout.btn_down = NavButton(nav='camera_screen', size_hint=(.35, .5), text='Вниз')

        self.main_layout.btn_up.pos_hint = {'center_x': 0.5}
        self.main_layout.btn_down.pos_hint = {'center_x': 0.5}

        self.add_widget(self.fon_image)
        self.main_layout.add_widget(self.main_layout.btn_up)
        self.main_layout.layout.add_widget(self.main_layout.layout.btn_left)
        self.main_layout.layout.add_widget(self.main_layout.layout.text)
        self.main_layout.layout.add_widget(self.main_layout.layout.btn_right)
        self.main_layout.add_widget(self.main_layout.layout)
        self.main_layout.add_widget(self.main_layout.btn_down)

        self.add_widget(self.main_layout)


class PointsScreen(Screen):
    """Экран с точками"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(orientation='vertical')
        self.main_layout.can = Widget()
        self.main_layout.layout = BoxLayout(orientation='horizontal', size_hint=(1, None))
        self.main_layout.layout.plus100_btn = PlusButton(pl=100, text='+100')
        self.main_layout.layout.plus500_btn = PlusButton(pl=500, text='+500')
        self.main_layout.layout.reset_btn = ResetButton(canv=self.main_layout.can, text='reset')
        self.main_layout.layout.count = Label(text='0')
        self.main_layout.layout.back_btn = NavButton(nav='main_screen', text='Назад', clear=True, canv=self.main_layout.can)

        self.main_layout.add_widget(self.main_layout.can)
        self.main_layout.layout.add_widget(self.main_layout.layout.plus100_btn)
        self.main_layout.layout.add_widget(self.main_layout.layout.plus500_btn)
        self.main_layout.layout.add_widget(self.main_layout.layout.reset_btn)
        self.main_layout.layout.add_widget(self.main_layout.layout.count)
        self.main_layout.layout.add_widget(self.main_layout.layout.back_btn)
        self.main_layout.add_widget(self.main_layout.layout)
        self.add_widget(self.main_layout)


class DrawScreen(Screen):
    """Экран для рисования"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation='vertical')
        self.main_layout.can = Drawcanvas()
        self.main_layout.layout = BoxLayout(orientation='horizontal', size_hint=(1, .4))
        self.main_layout.layout.color_layout = BoxLayout(orientation='vertical')
        self.main_layout.layout.color_layout.red_slider = ColorSlider(color='red', min=0, max=255, value_track=True, value_track_color=[1, 0, 0, 1])
        self.main_layout.layout.color_layout.green_slider = ColorSlider(color='green', min=0, max=255, value_track=True, value_track_color=[0, 1, 0, 1])
        self.main_layout.layout.color_layout.blue_slider = ColorSlider(color='blue', min=0, max=255, value_track=True, value_track_color=[0, 0, 1, 1])
        self.main_layout.layout.col = Label(size_hint=(.3, 1))
        self.main_layout.layout.reset_btn = ResetButton(canv=self.main_layout.can, text='Стереть', size_hint=(.4, 1))
        self.main_layout.layout.back_btn = NavButton(text='назад', nav='main_screen', size_hint=(.4, 1), clear=True, canv=self.main_layout.can)

        self.main_layout.add_widget(self.main_layout.can)
        self.main_layout.add_widget(self.main_layout.layout)
        self.main_layout.layout.color_layout.add_widget(self.main_layout.layout.color_layout.red_slider)
        self.main_layout.layout.color_layout.add_widget(self.main_layout.layout.color_layout.green_slider)
        self.main_layout.layout.color_layout.add_widget(self.main_layout.layout.color_layout.blue_slider)
        self.main_layout.layout.add_widget(self.main_layout.layout.color_layout)
        self.main_layout.layout.add_widget(self.main_layout.layout.col)
        self.main_layout.layout.add_widget(self.main_layout.layout.reset_btn)
        self.main_layout.layout.add_widget(self.main_layout.layout.back_btn)

        self.add_widget(self.main_layout)


class ProtectedScreen(Screen):
    """Экран с паролем"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.fon_image = Image(source=PRISON, fit_mode='fill')
        self.main_layout = BoxLayout(orientation='vertical')
        self.main_layout.txt = Label(text='Введите пароль', size_hint=(1, .5))
        self.main_layout.text_input = TextInput(size_hint=(.5, .1), halign='left', multiline=False)
        self.main_layout.layout = BoxLayout(orientation='horizontal', size_hint=(.5, .5), padding=20, spacing=20)
        self.main_layout.layout.apply = NavButton(nav='apply', text='ОК!', size_hint=(.8, .5))
        self.main_layout.layout.back = NavButton(nav='main_screen', text='назад', size_hint=(.8, .5))

        self.main_layout.text_input.pos_hint = {'center_x': 0.5, 'center_y': 1}
        self.main_layout.layout.pos_hint = {'center_x': 0.5}
        self.main_layout.layout.apply.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.main_layout.layout.back.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.add_widget(self.fon_image)
        self.main_layout.add_widget(self.main_layout.txt)
        self.main_layout.add_widget(self.main_layout.text_input)
        self.main_layout.layout.add_widget(self.main_layout.layout.apply)
        self.main_layout.layout.add_widget(self.main_layout.layout.back)
        self.main_layout.add_widget(self.main_layout.layout)

        self.add_widget(self.main_layout)


class ImageScreen(Screen):
    """Экран с картинкой"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(orientation='vertical')
        self.main_layout.image = Image(source=POOP, size_hint=(None, None), width=100, height=100)
        self.main_layout.layout = BoxLayout(orientation='horizontal')
        self.main_layout.layout.txt = Label(text='Не трогай меня!')
        self.main_layout.layout.back_btn = NavButton(nav='main_screen', clear=True, text='Назад', size_hint=(None, None), width='100sp', height='100sp')

        self.main_layout.layout.back_btn.pos_hint = {'right': 1}
        self.main_layout.image.pos_hint = {'center_x': 0.5}
        self.main_layout.layout.txt.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.main_layout.image.on_touch_down = self.change_image

        self.main_layout.layout.add_widget(self.main_layout.layout.txt)
        self.main_layout.layout.add_widget(self.main_layout.layout.back_btn)
        self.main_layout.add_widget(self.main_layout.image)
        self.main_layout.add_widget(self.main_layout.layout)

        self.add_widget(self.main_layout)

    def change_image(self, touch):
        """Изменяет размеры изображения"""
        if self.main_layout.image.width > 600:
            self.main_layout.layout.txt.text = 'Ты пожалеешь...'
        if self.main_layout.image.width > 1200:
            self.main_layout.image.source = SCRIM
            self.main_layout.layout.txt.text = 'ААААААААААААААА'
            return
        self.main_layout.image.width += 50
        self.main_layout.image.height += 50


class CameraScreen(Screen):
    """Экран с камерой"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(orientation='vertical')
        self.main_layout.image = Image(source='', fit_mode='fill')
        self.main_layout.layout = BoxLayout(orientation='horizontal', size_hint=(1, .2))
        self.main_layout.layout.start_btn = Button(text='сфоткать')
        self.main_layout.layout.back_btn = NavButton(nav='main_screen', clear=True, text='Назад')

        self.main_layout.layout.start_btn.on_press = self.click

        self.main_layout.add_widget(self.main_layout.image)
        self.main_layout.layout.add_widget(self.main_layout.layout.start_btn)
        self.main_layout.layout.add_widget(self.main_layout.layout.back_btn)
        self.main_layout.add_widget(self.main_layout.layout)
        self.add_widget(self.main_layout)

    def click(self):
        """Меняет картинку"""

        while True:
            new_image = choice(FACES)
            if new_image != self.main_layout.image.source:
                self.main_layout.image.source = new_image
                break


class NavButton(Button):
    """Навигационные кнопки"""

    def __init__(self, nav, clear=False, canv=None, **kwargs):
        super().__init__(**kwargs)
        self.nav = nav
        self.canv = canv
        self.clear = clear
        self.on_press = self.next

    def next(self):
        """Переключает экран при нажатии"""

        global r, g, b

        if self.clear:

            if self.canv is not None:
                self.canv.canvas.clear()
            app.points_screen.main_layout.layout.count.text = '0'
            app.draw_screen.main_layout.layout.color_layout.red_slider.value = 0
            app.draw_screen.main_layout.layout.color_layout.green_slider.value = 0
            app.draw_screen.main_layout.layout.color_layout.blue_slider.value = 0
            r, g, b = 0, 0, 0

            with app.draw_screen.main_layout.layout.col.canvas:
                Color(0, 0, 0, 1)
                Rectangle(pos=app.draw_screen.main_layout.layout.col.pos, size=app.draw_screen.main_layout.layout.col.size)

            app.image_screen.main_layout.image.width = 100
            app.image_screen.main_layout.image.height = 100
            app.image_screen.main_layout.image.source = POOP
            app.image_screen.main_layout.layout.txt.text = 'Не трогай меня!'
            app.camera_screen.main_layout.image.source = ''

        if self.nav == 'points_screen':
            app.position = 'up'
            app.main_screen.manager.transition.direction = 'down'
            app.main_screen.manager.current = 'protected_screen'

        if self.nav == 'camera_screen':
            app.position = 'down'
            app.main_screen.manager.transition.direction = 'up'
            app.main_screen.manager.current = 'protected_screen'

        if self.nav == 'draw_screen':
            app.position = 'left'
            app.main_screen.manager.transition.direction = 'right'
            app.main_screen.manager.current = 'protected_screen'

        if self.nav == 'image_screen':
            app.position = 'right'
            app.main_screen.manager.transition.direction = 'left'
            app.main_screen.manager.current = 'protected_screen'

        if self.nav == 'main_screen':
            app.main_screen.manager.transition.direction = app.position
            app.protected_screen.main_layout.text_input.text = ''
            app.protected_screen.main_layout.txt.text = 'Введите пароль'
            app.protected_screen.main_layout.txt.color = 'white'
            app.main_screen.manager.current = 'main_screen'

        if self.nav == 'apply':

            if app.protected_screen.main_layout.text_input.text.lower() == PASSWORD.lower() or app.protected_screen.main_layout.text_input.text.lower() == '1':

                if app.position == 'up':
                    app.main_screen.manager.current = 'points_screen'

                elif app.position == 'down':
                    app.main_screen.manager.current = 'camera_screen'

                elif app.position == 'left':
                    app.main_screen.manager.current = 'draw_screen'

                elif app.position == 'right':
                    app.main_screen.manager.current = 'image_screen'

            else:
                app.protected_screen.main_layout.txt.text = 'Неверный пароль'
                app.protected_screen.main_layout.txt.color = 'red'


class PlusButton(Button):
    """КНОПКИ ДОБАЛЯЮЩИЕ ТОЧКИ"""

    def __init__(self, pl, **kwargs):
        super().__init__(**kwargs)
        self.pl = pl
        self.on_press = self.plus_points

    def plus_points(self):
        """Добавление точек"""

        with app.points_screen.main_layout.can.canvas:
            app.points_screen.main_layout.layout.count.text = str(
                int(app.points_screen.main_layout.layout.count.text) + self.pl)
            for i in range(self.pl):
                R, G, B, A = rand(0, 255) / 256, rand(0, 255) / 256, rand(0, 255) / 256, 1
                Color(R, G, B, A)
                Rectangle(pos=(rand(0, 1080), rand(0, 1920)), size=(10, 10))


class ResetButton(Button):
    """Кнопка очищает холст"""

    def __init__(self, canv, **kwargs):
        super().__init__(**kwargs)
        self.on_press = self.reset
        self.canv = canv

    def reset(self):
        """очистка холста"""
        self.canv.canvas.clear()
        app.points_screen.main_layout.layout.count.text = '0'


class ColorSlider(Slider):
    """Слайдеры цвета"""

    def __init__(self, color, **kwargs):
        global r, g, b
        super().__init__(**kwargs)
        self.color = color

        if color == 'red':
            r = self.value

        if color == 'green':
            g = self.value

        if color == 'blue':
            b = self.value

        self.bind(value=self.change)

    def change(self, instance, brightness):
        """Обрабатывает изменения значений ползунков"""
        global r, g, b
        if self.color == 'red':
            r = self.value

        if self.color == 'green':
            g = self.value

        if self.color == 'blue':
            b = self.value

        with app.draw_screen.main_layout.layout.col.canvas:
            Color(r / 256, g / 256, b / 256, 0.1)
            Rectangle(pos=app.draw_screen.main_layout.layout.col.pos, size=app.draw_screen.main_layout.layout.col.size)


class Drawcanvas(Widget):
    """Холст для рисунков"""

    def on_touch_down(self, touch):
        if touch.y < 480: return
        with self.canvas:
            Color(r / 256, g / 256, b / 256, 1)
            Ellipse(pos=(touch.x - RAD / 2, touch.y - RAD / 2), size=(RAD, RAD))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=RAD / 2)

    def on_touch_move(self, touch):
        if touch.y < 480: return
        try:
            touch.ud['line'].points += touch.x, touch.y
        except Exception:
            pass


if __name__ == '__main__':
    app = Applick()
    app.run()
