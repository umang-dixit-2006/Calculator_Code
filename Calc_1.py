"""
This is a simple calculator application built using Tkinter in Python.

It supports basic arithmetic operations including addition, subtraction,
multiplication, division, percentage, and decimal points. The calculator
also supports clear entry and clear all operations.

This is the optimized version of the calculator code with improved functionality
and better handling of user inputs.

It aslo handle errors like division by zero and invalid expressions and exceptions are also written.

You can also see the other code version named 'Calculator.py' for comparison in the same folder.
"""

from tkinter import *
import tkinter.ttk as ttk

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.geometry('500x500')
        self.window.title('Calculator')
        
        # Expression variables
        self.expression = ""
        self.result_displayed = False
        
        # Create and place the entry widget
        self.e = ttk.Entry(window, width=34, font=('Arial', 14))
        self.e.place(x=10, y=10)
        
        # Create buttons
        self.create_buttons()
        
    def create_buttons(self):
        # Button layout configuration
        button_config = [
            # (text, x, y, command, width)
            ('7', 10, 50, lambda: self.click('7'), 10),
            ('8', 80, 50, lambda: self.click('8'), 10),
            ('9', 150, 50, lambda: self.click('9'), 10),
            ('÷', 220, 50, lambda: self.operation('/'), 10),
            ('CE', 290, 50, self.clear_entry, 10),
            
            ('4', 10, 85, lambda: self.click('4'), 10),
            ('5', 80, 85, lambda: self.click('5'), 10),
            ('6', 150, 85, lambda: self.click('6'), 10),
            ('×', 220, 85, lambda: self.operation('*'), 10),
            ('C', 290, 85, self.clear_all, 10),
            
            ('1', 10, 120, lambda: self.click('1'), 10),
            ('2', 80, 120, lambda: self.click('2'), 10),
            ('3', 150, 120, lambda: self.click('3'), 10),
            ('-', 220, 120, lambda: self.operation('-'), 10),
            ('⌫', 290, 120, self.delete, 10),
            
            ('0', 10, 155, lambda: self.click('0'), 10),
            ('.', 80, 155, lambda: self.click('.'), 10),
            ('%', 150, 155, lambda: self.operation('%'), 10),
            ('+', 220, 155, lambda: self.operation('+'), 10),
            ('=', 290, 155, self.equals, 10)
        ]
        
        # Create buttons using the configuration
        for text, x, y, command, width in button_config:
            ttk.Button(
                self.window, 
                text=text, 
                width=width, 
                command=command
            ).place(x=x, y=y)
    
    def click(self, num):
        if self.result_displayed:
            self.e.delete(0, END)
            self.result_displayed = False
        
        current = self.e.get()
        self.e.delete(0, END)
        
        # Prevent multiple decimal points in a number
        if num == '.':
            # Find the last number in the expression
            last_number = self.get_last_number(current)
            if '.' in last_number:
                self.e.insert(0, current)
                return
        
        self.e.insert(0, current + str(num))
    
    def get_last_number(self, expression):
        """Extract the last number from the expression"""
        # Remove operators and split
        operators = ['+', '-', '*', '/', '%', '**', '//']
        for op in operators:
            expression = expression.replace(op, ' ')
        
        # Get the last element
        parts = expression.split()
        return parts[-1] if parts else ""
    
    def operation(self, op):
        if self.result_displayed:
            self.result_displayed = False
        
        current = self.e.get()
        
        # If entry is empty, start with 0
        if not current:
            current = "0"
        
        # Replace × with * for calculation
        display_op = '×' if op == '*' else op
        
        # Check if last character is an operator
        operators = ['+', '-', '*', '/', '%', '**', '//', '×']
        if current and current[-1] in operators:
            # Replace the last operator
            self.e.delete(0, END)
            self.e.insert(0, current[:-1] + display_op)
        else:
            self.e.insert(END, display_op)
    
    def clear_entry(self):
        """Clear only the current entry"""
        self.e.delete(0, END)
    
    def clear_all(self):
        """Clear everything"""
        self.e.delete(0, END)
        self.expression = ""
        self.result_displayed = False
    
    def delete(self):
        """Delete last character"""
        current = self.e.get()
        if current:
            self.e.delete(0, END)
            self.e.insert(0, current[:-1])
    
    def equals(self):
        try:
            # Get the expression from entry
            expression = self.e.get()
            
            # Replace display operators with calculation operators
            expression = expression.replace('×', '*')
            
            # Validate expression
            if not expression:
                return
            
            # Check for balanced parentheses
            if expression.count('(') != expression.count(')'):
                self.e.delete(0, END)
                self.e.insert(0, "Error: Unbalanced parentheses")
                return
            
            # Evaluate the expression
            result = eval(expression)
            
            # Format result
            if isinstance(result, float):
                # Limit decimal places to avoid floating point errors
                result = round(result, 10)
                # Remove trailing zeros
                result = result if result != int(result) else int(result)
            
            # Display result
            self.e.delete(0, END)
            self.e.insert(0, str(result))
            self.result_displayed = True
            
        except ZeroDivisionError:
            self.e.delete(0, END)
            self.e.insert(0, "Error: Division by zero")
            self.result_displayed = True
        except SyntaxError:
            self.e.delete(0, END)
            self.e.insert(0, "Error: Invalid expression")
            self.result_displayed = True
        except Exception as e:
            self.e.delete(0, END)
            self.e.insert(0, f"Error: {str(e)}")
            self.result_displayed = True

# Create the main window
window = Tk()
calculator = Calculator(window)
window.mainloop()
