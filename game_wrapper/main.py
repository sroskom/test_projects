from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Rectangle
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label

class Global():
    debugMode = False

class Top(Widget):
    def __init__(self,*args):
        super(Top,self).__init__(*args)
        self.size = Window.size
        self.add_widget(MainMenu(size=self.size))

class GameArea(Widget):
    def __init__(self,size,*args):
        super(GameArea,self).__init__(size=size,*args)
        self.add_widget(Label(text='replace this widget \n with your game',
                              size=size,
                              font_size=20))

class SettingsScreen(Widget):
    def __init__(self,size,*args):
        super(SettingsScreen,self).__init__(size=size,*args)
        button_height = self.height*.10
        button_size = [button_height*6,button_height]
        self.option_1 = Label(text=('debug:on' if Global.debugMode
                                    else 'debug:off'),
                              size=button_size,
                              font_size=button_size[1],
                              pos=[0,self.height*.60])
        self.option_2 = Label(text='back',
                              size=button_size,
                              font_size=button_size[1],
                              pos=[0,self.height*.30])
        self.option_1.center_x = self.center_x
        self.option_2.center_x = self.center_x
        self.add_widget(self.option_1)
        self.add_widget(self.option_2)
        
    def on_touch_down(self,touch,*args):
        super(SettingsScreen,self).on_touch_down(touch,*args)
        if self.option_1.collide_point(*touch.pos):
            if not Global.debugMode:
                self.option_1.text = 'debug:on'
                Global.debugMode = True
            else:
                self.option_1.text = 'debug:off'
                Global.debugMode = False
        elif self.option_2.collide_point(*touch.pos):
            self.parent.add_widget(MainMenu(size=self.size))
            self.parent.remove_widget(self)
        
class MainMenu(Widget):
    def __init__(self,size,*args):
        super(MainMenu,self).__init__(size=size,*args)
        
        button_height = self.height*.10
        button_size = [button_height*5,button_height]
        self.option_1 = Label(text='play game',
                              size=button_size,
                              font_size=button_size[1],
                              pos=[0,self.height*.60])
        self.option_2 = Label(text='settings',
                              size=button_size,
                              font_size=button_size[1],
                              pos=[0,self.height*.30])
        self.option_1.center_x = self.center_x
        self.option_2.center_x = self.center_x
        self.add_widget(self.option_1)
        self.add_widget(self.option_2)
        
    def on_touch_down(self,touch,*args):
        super(MainMenu,self).on_touch_down(touch,*args)
        if self.option_1.collide_point(*touch.pos):
            self.parent.add_widget(GameArea(size=self.size))
            self.parent.remove_widget(self)
        elif self.option_2.collide_point(*touch.pos):
            self.parent.add_widget(SettingsScreen(size=self.size))
            self.parent.remove_widget(self)
        
        
class GameApp(App):
    def on_pause(self,*args):
        return True
    
    def build(self,*args):
        return Top()

if __name__=='__main__':
    #Window.size = 300,450
    GameApp().run()
