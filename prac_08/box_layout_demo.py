from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Box layout model for app."""
    def build(self):
        """Build the app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle a button press to display message from text input to an output label."""
        # print('test')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle a button press to clear text input and label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
