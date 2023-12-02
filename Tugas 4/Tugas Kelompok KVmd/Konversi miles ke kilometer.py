from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

class UnitConverterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.title = "Miles to Kilometers Converter"  # Judul aplikasi
        self.root = MDBoxLayout(orientation='vertical', padding=10)

        self.input_field = MDTextField(
            hint_text="Enter value",
            helper_text="Enter the value to convert",
            helper_text_mode="on_focus",
        )
        self.root.add_widget(self.input_field)

        self.result_label = MDTextField(
            readonly=True,
            hint_text="Result",
            helper_text="Conversion result",
            helper_text_mode="on_focus",
        )
        self.root.add_widget(self.result_label)

        self.convert_button = MDRaisedButton(
            text="Convert",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.convert_unit,
        )
        self.root.add_widget(self.convert_button)

        return self.root

    def convert_unit(self, instance):
        try:
            input_value = float(self.input_field.text)
            result = input_value * 1.60934  # Convert miles to kilometers
            self.result_label.text = f"Result: {result:.2f} km"
        except ValueError:
            self.result_label.text = "Invalid input"

if __name__ == "__main__":
    UnitConverterApp().run()