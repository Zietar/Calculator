import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("250x200")

calculations = ""

def button_click(value):
    global calculations
    if value == 'C':
        calculations = ""
    elif value == '=':
        try:
            calculations = str(eval(calculations.replace('x', '*')))
        except Exception:
            calculations = "Error"
    else:
        if value in ['+', '-', 'x', '/'] and calculations[-1] in ['+', '-', 'x', '/']:
            calculations = calculations[:-1]
        calculations += value

    result_label.config(text=calculations)

# 0 ROW
result_label = tk.Label(root)
result_label.grid(column=0, columnspan=4, padx=5, pady=5)

# 1 ROW
button_7 = tk.Button(root, text='7', command=lambda: button_click('7'))
button_7.grid(row=1, column=0, padx=5, pady=5)

button_8 = tk.Button(root, text='8', command=lambda: button_click('8'))
button_8.grid(row=1, column=1, padx=5, pady=5)

button_9 = tk.Button(root, text='9', command=lambda: button_click('9'))
button_9.grid(row=1, column=2, padx=5, pady=5)

button_addition = tk.Button(root, text='+', command=lambda: button_click('+'))
button_addition.grid(row=1, column=3, padx=5, pady=5)

# 2 ROW
button_4 = tk.Button(root, text='4', command=lambda: button_click('4'))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = tk.Button(root, text='5', command=lambda: button_click('5'))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = tk.Button(root, text='6', command=lambda: button_click('6'))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_subtraction = tk.Button(root, text='-', command=lambda: button_click('-'))
button_subtraction.grid(row=2, column=3, padx=5, pady=5)

# 3 ROW
button_1 = tk.Button(root, text='1', command=lambda: button_click('1'))
button_1.grid(row=3, column=0, padx=5, pady=5)

button_2 = tk.Button(root, text='2', command=lambda: button_click('2'))
button_2.grid(row=3, column=1, padx=5, pady=5)

button_3 = tk.Button(root, text='3', command=lambda: button_click('3'))
button_3.grid(row=3, column=2, padx=5, pady=5)

button_multiplication = tk.Button(root, text='x', command=lambda: button_click('x'))
button_multiplication.grid(row=3, column=3, padx=5, pady=5)

# 4 ROW
button_C = tk.Button(root, text='C', command=lambda: button_click('C'))
button_C.grid(row=4, column=0, padx=5, pady=5)

button_0 = tk.Button(root, text='0', command=lambda: button_click('0'))
button_0.grid(row=4, column=1, padx=5, pady=5)

button_equals = tk.Button(root, text='=', command=lambda: button_click('='))
button_equals.grid(row=4, column=2, padx=5, pady=5)

button_division = tk.Button(root, text='/', command=lambda: button_click('/'))
button_division.grid(row=4, column=3, padx=5, pady=5)

root.mainloop()