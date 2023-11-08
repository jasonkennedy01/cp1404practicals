from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM_RATE = 1.60934


class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to Kms."""
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = ""
        return self.root

    def handle_increment(self, value, step):
        """"""
        try:
            new_value = int(value) + step
        except ValueError:
            new_value = 0 + step
        self.root.ids.input_miles.text = f"{new_value}"

    def handle_conversion(self, miles):
        """"""
        try:
            km = float(miles) * MILES_TO_KM_RATE
        except ValueError:
            km = 0.0

        self.message = f"{km}"


ConvertMilesKmApp().run()
