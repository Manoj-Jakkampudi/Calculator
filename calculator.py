import tkinter as tk
from tkinter import messagebox

# Function to update the display when a button is clicked
def on_button_click(value):
    current_text = display.get()
    if value == "=":
        try:
            # Evaluate the expression and display the result
            result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            # Add to history
            history.append(f"{current_text} = {result}")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == "C":
        # Clear the display
        display.delete(0, tk.END)
    else:
        # Append the clicked button's value to the display
        display.insert(tk.END, value)

# Function to show calculation history
def show_history():
    if not history:
        messagebox.showinfo("History", "No calculations yet!")
    else:
        history_text = "\n".join(history)
        messagebox.showinfo("Calculation History", history_text)

# Create the main application window
root = tk.Tk()
root.title("Graphical Calculator")
root.geometry("400x500")  # Adjusted size for better layout
root.resizable(False, False)

# Configure rows and columns to expand properly
for i in range(7):  # 7 rows (1 for display + 6 for buttons)
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns for buttons
    root.grid_columnconfigure(j, weight=1)

# Create the display widget
display = tk.Entry(root, font=("Arial", 24), justify="right", bd=10, relief="ridge", bg="#f0f0f0")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Define the buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("=", 5, 0)
]

# Add buttons to the grid
for text, row, col in buttons:
    action = lambda x=text: on_button_click(x)
    if text == "=":
        # Span the "=" button across all 4 columns
        btn = tk.Button(root, text=text, font=("Arial", 18), command=action, bg="#4CAF50", fg="white")
        btn.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=5, pady=5)
    else:
        # Regular buttons
        btn = tk.Button(root, text=text, font=("Arial", 18), command=action, bg="#2196F3", fg="white")
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Add History button
history_button = tk.Button(root, text="History", font=("Arial", 18), command=show_history, bg="#FFC107", fg="white")
history_button.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# History storage
history = []

# Run the application
root.mainloop()