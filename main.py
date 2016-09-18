'''Up2Seconds application.'''

import kivy
from kivy.app import App
from screens.manager import AppScreenManager
from screens.startscreen import StartScreen


class KivyLazyloadingExampleApp(App):
    '''Main kivy application class.'''

    def build(self):
        '''Sets AppScreenManager as root widget.'''
        sm = AppScreenManager()
        sm.add_widget(StartScreen())
        return sm

    def on_start(self):
        '''Configures app when it starts.'''
        self.use_kivy_settings = False

    def open_settings(self):
        '''Prevents the settings panel from opening.'''
        pass

    def on_pause(self):
        '''Background persistence support for Android/iOS.'''
        return True


if __name__ == '__main__':
    KivyLazyloadingExampleApp().run()
