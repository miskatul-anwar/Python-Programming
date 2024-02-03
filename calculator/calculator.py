from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.operand1 = ''
        self.operand2 = ''
        self.operation = ''
        
        layout = GridLayout(cols=4, spacing=5)

        self.result_text = TextInput(multiline=False, readonly=True, font_size=40, size_hint=(1, 0.5))
        layout.add_widget(self.result_text)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text, font_size=40)
            button.bind(on_press=self.on_button_press)
            layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        button_text = instance.text

        if button_text.isdigit() or button_text == '.':
            if self.operation == '':
                self.operand1 += button_text
                self.update_display(self.operand1)
            else:
                self.operand2 += button_text
                self.update_display(self.operand2)
        elif button_text in ['+', '-', '*', '/']:
            self.operation = button_text
        elif button_text == '=':
            if self.operation and self.operand1 and self.operand2:
                result = self.calculate_result()
                self.update_display(result)
                self.operand1 = str(result)
                self.operand2 = ''
                self.operation = ''
        elif button_text == 'C':
            self.operand1 = ''
            self.operand2 = ''
            self.operation = ''
            self.update_display('')

    def calculate_result(self):
        if self.operation == '+':
            return float(self.operand1) + float(self.operand2)
        elif self.operation == '-':
            return float(self.operand1) - float(self.operand2)
        elif self.operation == '*':
            return float(self.operand1) * float(self.operand2)
        elif self.operation == '/':
            try:
                return float(self.operand1) / float(self.operand2)
            except ZeroDivisionError:
                return 'Error: Division by zero'

    def update_display(self, value):
        self.result_text.text = str(value)


if __name__ == '__main__':
    CalculatorApp().run()
