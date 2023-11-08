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

    def handle_increment(self, value, step):
        try:
            new_value = int(value) + step
        except ValueError:
            pass
        self.root.ids.input_miles.text = f"{new_value}"

    def handle_conversion(self, miles):
        try:
            km = float(miles) * 1.60934
        except ValueError:
            pass
        self.root.ids.output_label.text = f"{km}"


ConvertMilesKmApp().run()
