#calculator app

import tkinter as tk
from tkinter import ttk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(symbol))
    
def button_clear():
    entry.delete(0, tk.END)
    
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
        
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Syntax Error")
        
def exit_app():
    root.destroy()
      
root = tk.Tk()
root.title('@Dev_aladinh production')
root.geometry('678x440')
root.resizable(False, False)
root.configure(bg="#008080") 

entry = tk.Entry(root, font=("Georgia", 20), width=20, borderwidth=10, relief="solid", bg="#D9D9D9", justify="center")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

style = ttk.Style()
style.configure("TButton", font=("Times New Roman", 16), padding=15)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('(', 1, 2), ('/', 1, 3),
    ('3', 2, 0), ('4', 2, 1), (')', 2, 2), ('*', 2, 3),
    ('5', 3, 0), ('6', 3, 1), ('.', 3, 2), ('-', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('9', 5, 0), ('0', 5, 1), ('Clear', 5, 2) 
]

for (text, row, col) in buttons:
    if text == 'Clear':
        command = button_clear
    elif text == '=':
        command = button_equal
    else:
        command = lambda t=text: button_click(t)
        
    button = ttk.Button(root, text=text, command=command, style="TButton")
    button.grid(row=row, column=col, padx=5, pady=5)

exit_button = ttk.Button(root, text='Exit', command=exit_app, style="TButton", cursor="hand2")
exit_button.grid(row=5, column=3, columnspan=4, padx=5, pady=10)

root.mainloop()
