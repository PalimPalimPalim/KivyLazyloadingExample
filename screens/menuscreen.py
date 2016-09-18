'''Menu screen.'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('menuscreen.kv')


class MenuScreen(Screen):
    '''Screen class.'''

    def login(self):
        if not self.manager.has_screen('FeedScreen'):
            from feedscreen import FeedScreen
            self.manager.add_widget(FeedScreen())
        self.manager.current = 'FeedScreen'
