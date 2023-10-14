# Import necessary Kivy modules
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

# Define a Kivy application class named CalculatorApp
class CalculatorApp(App):
    def build(self):
        # Create the main layout widget, a vertical BoxLayout
        root_widget = BoxLayout(orientation='vertical')
        
        # Create the output label widget with a large font size
        output_label = Label(size_hint_y=0.75, font_size=50)
        
        # Define a list of button symbols for the calculator
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        
        # Create a grid layout for the buttons with 4 columns and a height that is twice the default
        button_grid = GridLayout(cols=4, size_hint_y=2)
        
        # Add buttons to the grid layout with their respective symbols
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))
        
        # Create a "Clear" button with a specific height
        clear_button = Button(text='Clear', size_hint_y=None, height=100)
        
        # Define a function to print the text of the pressed button to the output label
        def print_button_text(instance):
            output_label.text += instance.text
        
        # Bind the print_button_text function to all buttons in the grid (except the first one)
        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)
        
        # Define a function to resize the label text based on its height
        def resize_label_text(label, new_height):
            label.font_size = 0.5 * label.height
        
        # Bind the resize_label_text function to the output label's height property
        output_label.bind(height=resize_label_text)
        
        # Define a function to evaluate the result when the "=" button is pressed
        def evaluate_result(instance):
            try:
                # Evaluate the expression in the output label and update the label text
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                # Handle syntax errors by displaying an error message
                output_label.text = 'Python Syntax error!'
        
        # Bind the evaluate_result function to the "=" button
        button_grid.children[0].bind(on_press=evaluate_result)
        
        # Define a function to clear the output label
        def clear_label(instance):
            output_label.text = " "
        
        # Bind the clear_label function to the "Clear" button
        clear_button.bind(on_press=clear_label)
        
        # Add the output label, button grid, and "Clear" button to the main layout
        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)
        
        # Return the main layout as the root widget for the application
        return root_widget

# Create an instance of the CalculatorApp and run the application
CalculatorApp().run()
