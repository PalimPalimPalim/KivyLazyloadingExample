'''Start screen.'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('startscreen.kv')


class StartScreen(Screen):
    '''Screen class.'''

    def start(self):
        if not self.manager.has_screen('MenuScreen'):
            from menuscreen import MenuScreen
            self.manager.add_widget(MenuScreen())
        self.manager.current = 'MenuScreen'
