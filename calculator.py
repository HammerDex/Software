import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Simple Calculator - COMP2116")
root.geometry("320x280")

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"Result: {result}")
    except:
        label_result.config(text="Input Error!")

# Input text box
entry = ttk.Entry(root, font=('Arial', 18), justify='center')
entry.pack(pady=20, padx=20, fill='x')

# Calculate button
btn = ttk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=5)

# Result display label
label_result = ttk.Label(root, text="Result:", font=('Arial', 16))
label_result.pack(pady=20)

root.mainloop()