from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from filesharer import FileSharer

import time
import webbrowser

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.output_path = None

    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y_%m_%d-%H_%M_%S')
        self.output_path = f"./output/{current_time}.png"
        self.ids.camera.export_to_png(self.output_path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.image_id.source = self.output_path


class ImageScreen(Screen):
    link_message = 'Please, Create a Link First'

    def __init__(self, **kw):
        super().__init__()
        self.shared_link = None

    def create_link(self):

        output_path = App.get_running_app().root.ids.camera_screen.output_path
        filesharer = FileSharer(filepath=output_path)
        self.shared_link = filesharer.share()

        # upload label
        self.ids.label_share_id.text = self.shared_link

    def copy_link(self):

        if self.shared_link is None:
            self.ids.label_share_id.text = self.link_message
        else:
            Clipboard.copy(self.shared_link)


    def open_link(self):
        try:
            webbrowser.open(self.shared_link)
        except:
            self.ids.label_share_id.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
