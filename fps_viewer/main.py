from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from SpriteAnimator import SpriteAnimator


class GameApp(App):
    def update(self,*args):
        self.label_fps.text = 'fps:'+ str(Clock.get_fps())
        self.label_rfps.text = 'rfps:'+ str(Clock.get_rfps())
    
    def build(self,*args):
        self.spriteanimator = SpriteAnimator(imgdir='capman.png')
    
        self.movinglabel = Label(text='moving')
        self.label_fps = Label(text='fps:')
        self.label_rfps = Label(text='rfps:')
    
        boxlayout = BoxLayout(orientation='vertical')
        boxlayout.add_widget(self.label_fps)
        boxlayout.add_widget(self.label_rfps)

        bxbot = BoxLayout()
        for i in range(0,3):
            bxbot.add_widget(SpriteAnimator(imgdir='capman.png'))
        
        boxlayout.add_widget(bxbot)
        return boxlayout

if __name__=='__main__':
    game = GameApp()
    Clock.schedule_interval(game.update,1.0/60.0)
    game.run()
    
