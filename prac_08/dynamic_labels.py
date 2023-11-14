""""""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Dynamic Label App model class"""

    def __init__(self):
        """Create the main app."""
        super().__init__()
        self.names = ["Jason Kennedy", "Reece Kelly", "Keanu Reeves", "Joe Money"]

    def build(self):
        """Build the app GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Creates labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
