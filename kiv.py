# import os
# os.environ['KIVY_NO_CONSOLELOG'] = 'hide'

from kivy.app import App
from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from random import randint as rand


PASSWORD = '1'
points = []


class Applick(App):
    """ГЛАВНЫЙ КЛАСС"""

    title = 'Приложение'

    def build(self):
        """строитель"""

        self.sm = ScreenManager()
        self.main_screen = MainScreen(name='main_screen')
        # self.left_screen = ChildScreen(name='left_screen', text='левый экран')
        self.points_screen = PointsScreen(name='points_screen')
        # self.right_screen = ChildScreen(name='right_screen', text='правый экран')
        # self.down_screen = ChildScreen(name='down_screen', text='нижний экран')
        self.protected_screen = ProtectedScreen(name='protected_screen')

        self.sm.add_widget(self.main_screen)
        # self.sm.add_widget(self.left_screen)
        self.sm.add_widget(self.points_screen)
        # self.sm.add_widget(self.right_screen)
        # self.sm.add_widget(self.down_screen)
        self.sm.add_widget(self.protected_screen)

        return self.sm


class MainScreen(Screen):
    """ГЛАВНЫЙ ЭКРАН"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.main_layout.btn_up = NavButton(nav='up_screen', size_hint=(.35, .5), text='Вверх')
        self.main_layout.layout = BoxLayout(orientation='horizontal', padding=8, spacing=8, size_hint=(1, .5))
        self.main_layout.layout.btn_left = NavButton(nav='left_screen', text='Влево')
        self.main_layout.layout.btn_right = NavButton(nav='right_screen', text='Вправо')
        self.main_layout.layout.text = Label(text='Выбери')
        self.main_layout.btn_down = NavButton(nav='down_screen', size_hint=(.35, .5), text='Вниз')

        self.main_layout.btn_up.pos_hint = {'center_x': 0.5}
        self.main_layout.btn_down.pos_hint = {'center_x': 0.5}

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
        self.main_layout.layout.reset_btn = ResetButton(text='reset')
        self.main_layout.layout.back_btn = NavButton(nav='main_screen', text='Назад', clear=True)

        self.main_layout.add_widget(self.main_layout.can)
        self.main_layout.layout.add_widget(self.main_layout.layout.plus100_btn)
        self.main_layout.layout.add_widget(self.main_layout.layout.plus500_btn)
        self.main_layout.layout.add_widget(self.main_layout.layout.reset_btn)
        self.main_layout.layout.add_widget(self.main_layout.layout.back_btn)
        self.main_layout.add_widget(self.main_layout.layout)
        self.add_widget(self.main_layout)


class ProtectedScreen(Screen):
    """Экран с паролем"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(orientation='vertical')
        self.main_layout.txt = Label(text='Введите пароль')
        self.main_layout.text_input = TextInput(size_hint=(.5, .1), halign='left', multiline=False)
        self.main_layout.layout = BoxLayout(orientation='horizontal', size_hint=(.5, .5))
        self.main_layout.layout.apply = NavButton(nav='apply', text='ОК!', size_hint=(.8, .5))
        self.main_layout.layout.back = NavButton(nav='main_screen', text='назад', size_hint=(.8, .5))

        self.main_layout.text_input.pos_hint = {'center_x': 0.5}
        self.main_layout.layout.pos_hint = {'center_x': 0.5}
        self.main_layout.layout.apply.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.main_layout.layout.back.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.main_layout.add_widget(self.main_layout.txt)
        self.main_layout.add_widget(self.main_layout.text_input)
        self.main_layout.layout.add_widget(self.main_layout.layout.apply)
        self.main_layout.layout.add_widget(self.main_layout.layout.back)
        self.main_layout.add_widget(self.main_layout.layout)

        self.add_widget(self.main_layout)


class NavButton(Button):
    """Навигационные кнопки"""

    def __init__(self, nav, clear=False, **kwargs):
        super().__init__(**kwargs)
        self.nav = nav
        self.clear = clear
        self.on_press = self.next

    def next(self):
        """Переключает экран при нажатии"""

        if self.clear:
            app.points_screen.main_layout.can.canvas.clear()

        if self.nav == 'up_screen':
            app.position = 'up'
            app.main_screen.manager.transition.direction = 'down'
            app.main_screen.manager.current = 'protected_screen'

        if self.nav == 'down_screen':
            app.position = 'down'
            app.main_screen.manager.transition.direction = 'up'
            app.main_screen.manager.current = 'protected_screen'

        if self.nav == 'left_screen':
            app.position = 'left'
            app.main_screen.manager.transition.direction = 'right'
            app.main_screen.manager.current = 'protected_screen'

        if self.nav == 'right_screen':
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

            if app.protected_screen.main_layout.text_input.text == PASSWORD:

                if app.position == 'up':
                    app.main_screen.manager.current = 'points_screen'

                elif app.position == 'down':
                    pass

                elif app.position == 'left':
                    pass

                elif app.position == 'right':
                    pass

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
        """Добавление"""
        with app.points_screen.main_layout.can.canvas:
            for i in range(self.pl):
                R, G, B, A = rand(0, 255) / 256, rand(0, 255) / 256, rand(0, 255) / 256, 1
                Color(R, G, B, A)
                Rectangle(pos=(rand(0, 600), rand(0, 600)), size=(10, 10))


class ResetButton(Button):
    """КНОПКА УБИРАЕТ ВСЕ ТОЧКИ"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_press = self.reset

    @staticmethod
    def reset():
        """очистка холста"""
        app.points_screen.main_layout.can.canvas.clear()


if __name__ == '__main__':
    app = Applick()
    app.run()
