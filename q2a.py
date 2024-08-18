import re
import tkinter as tk
from tkinter import messagebox

class BasicCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator GUI")

        # Main frame
        self.main_frame = tk.Frame(root, bg='lightgrey')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.input_field = tk.Entry(self.main_frame, width=40, font=('Arial', 14), borderwidth=2, relief='solid')
        self.result_label = tk.Label(self.main_frame, text="Result: ", font=('Arial', 14), bg='lightgrey')

        #Button grid
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('(', 4, 3),
            (')', 5, 0), ('C', 5, 1), ('=', 5, 2)
        ]
        
        # Create and place buttons
        for (text, row, col) in buttons:
            button = tk.Button(self.main_frame, text=text, font=('Arial', 14), bg='lightblue', padx=20, pady=10,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # Layout components
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.result_label.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.clear_input()
        elif char == '=':
            self.calculate_result()
        else:
            current_text = self.input_field.get()
            new_text = current_text + char
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, new_text)

    def calculate_result(self):
        expression = self.input_field.get().strip()
        try:
            result = self.evaluate_expression(expression)
            self.result_label.config(text=f"Result: {result:.2f}")
        except Exception as e:
            self.result_label.config(text="Error: Invalid expression")
            messagebox.showerror("Error", f"Invalid expression: {e}")

    def clear_input(self):
        self.input_field.delete(0, tk.END)
        self.result_label.config(text="Result: ")

    def evaluate_expression(self, expression):
        expression = self.clean_expression(expression)
        try:
            result = self.basic_calculator(expression)
            return result
        except Exception:
            raise ValueError("Invalid expression")

    def clean_expression(self, expression):
        expression = expression.replace(' ', '')
        if re.match(r'^[0-9+\-*/().]*$', expression):
            return expression
        raise ValueError("Expression contains invalid characters")

    def basic_calculator(self, expression):
        def eval_operator(op, val1, val2):
            if op == '+':
                return val1 + val2
            elif op == '-':
                return val1 - val2
            elif op == '*':
                return val1 * val2
            elif op == '/':
                if val2 == 0:
                    raise ValueError("Division by zero")
                return val1 / val2

        def parse(expression):
            num = 0
            stack = []
            op = '+'
            i = 0
            while i < len(expression):
                if expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                if (not expression[i].isdigit() and expression[i] != ' ') or i == len(expression) - 1:
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op in '*/':
                        stack[-1] = eval_operator(op, stack[-1], num)
                    num = 0
                    op = expression[i]
                i += 1
            return sum(stack)

        return parse(expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = BasicCalculatorGUI(root)
    root.mainloop()
