from kivy.app import App
from kivy.lang import Builder


from kivy.core.window import Window


class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to Kms."""

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKmApp().run()
