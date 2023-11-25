from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
from kivy.lang import Builder
import random 

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:
            title: "Rashin's Dice Roller"

    Image:
        id: dice_state
        name: 'dice_state'
        size_hint_y: 0.4
        size_hint_x: 0.4
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        source: "assets/dice_1.png"

    MDRectangleFlatButton:
        id: roll_button
        text: "Roll"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.play()
'''

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(Builder.load_string(KV))
        return screen
    
    def play(self):
        dice_face = random.choice(["dice_1.png", "dice_2.png", "dice_3.png", "dice_4.png", "dice_5.png", "dice_6.png"])
        file_name = "assets/" + dice_face 
        for widget in self.root.walk():
            if isinstance(widget, Image) and widget.name == 'dice_state':
                widget.source = file_name
                break

if __name__ == "__main__":
    MainApp().run()
