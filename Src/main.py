import os
from kivy.lang import Builder
from kivy.app import App

class LibraryApp(App):
    def build(self):
        kv_path = os.path.join(os.path.dirname(__file__), 'Presentation', 'first.kv')
        return Builder.load_file(kv_path)


if __name__ == "__main__":
    LibraryApp().run()