from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Rectangle


class Top(Widget):
    def __init__(self,*args):
        super(Top,self).__init__(*args)
        self.size = Window.size
        self.add_widget(Menu(size=self.size))

class Menu(Widget):
    def __init__(self,size,*args):
        super(Menu,self).__init__(size=size,*args)
        font_size = size[1]/10
        background = Image(source='images/background.png').texture
        background.wrap = 'repeat'
        
        
        aspectRatio = size[1]/float(background.size[1])
        x = (Window.width/background.size[0]//aspectRatio)+2
        print(x)
        background.uvsize = x,-1
        with self.canvas:
            rect = Rectangle(texture=background,
                             size=[(background.size[0]*
                                   aspectRatio*x),
                                   size[1]])
            
        boxlayout = BoxLayout(orientation='vertical',
                              size=size)
        boxlayout.add_widget(Label(text='tap to start',
                                   font_size=font_size))
        boxlayout.add_widget(Label(text='debug mode',
                                   font_size=font_size))
        self.add_widget(boxlayout)
        
class Game(Widget):
    pass

class GameApp(App):
    def on_pause(self,*args):
        return True
    
    def build(self,*args):
        return Top()

if __name__=='__main__':
    #simulate phone size
    Window.size = 300,450
    
    GameApp().run()
