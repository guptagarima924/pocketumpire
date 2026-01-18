from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera

class PocketUmpire(BoxLayout):
    def _init_(self, **kwargs):
        super()._init_(orientation='vertical', **kwargs)

        self.camera = Camera(resolution=(640,480), play=True)
        self.add_widget(self.camera)

        self.mark_btn = Button(text="MARK", size_hint=(1,0.2), background_color=(1,0,0,1))
        self.mark_btn.bind(on_press=self.mark)
        self.add_widget(self.mark_btn)

    def mark(self, instance):
        print("MARK pressed")

class PocketUmpireApp(App):
    def build(self):
        return PocketUmpire()

PocketUmpireApp().run()
