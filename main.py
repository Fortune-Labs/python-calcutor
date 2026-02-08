import tkinter as tk  # Import Tkinter and alias it as 'tk' for easier use

# Create the main application window
root = tk.Tk()  # Initialize the Tkinter root window
root.title("Simple Calculator")  # Set the window title
root.geometry("300x400")  # Set the window size (width x height)
root.resizable(False, False)  # Disable resizing (width, height)

# Create an Entry widget (text box) to display input and results
entry = tk.Entry(
    root,                     # Parent widget is the main window
    font=("Arial", 20),       # Font and size
    borderwidth=5,            # Thickness of the border
    relief="ridge",           # Border style
    justify="right"           # Align text to the right (calculator style)
)
entry.pack(fill="x", padx=10, pady=10)  # Place the entry at top, fill horizontally with padding

# ---- Calculator functions ----

def button_click(value):
    """Insert the pressed button's value into the entry box."""
    entry.insert(tk.END, value)  # Insert value at the end of current text

def clear():
    """Clear the entire entry box."""
    entry.delete(0, tk.END)  # Delete from index 0 to the end

def calculate():
    """Evaluate the expression in the entry box and show the result."""
    try:
        result = eval(entry.get())  # Evaluate the math expression string (e.g., "7+2*3")
        entry.delete(0, tk.END)     # Clear the entry box
        entry.insert(0, result)     # Insert the result at the start
    except:
        entry.delete(0, tk.END)     # Clear the entry box if error occurs
        entry.insert(0, "Error")    # Show "Error" if expression is invalid

# Define the calculator buttons in order (row by row)
buttons = [
    "7", "8", "9", "/",   # Row 1
    "4", "5", "6", "*",   # Row 2
    "1", "2", "3", "-",   # Row 3
    "0", ".", "=", "+"    # Row 4
]

# Create a Frame to hold the grid of number/operator buttons
frame = tk.Frame(root)  # Frame is inside the main window
frame.pack()            # Display the frame

row = 0  # Start grid row index
col = 0  # Start grid column index

# Create and place each button in the grid
for button in buttons:  # Loop through each button label
    if button == "=":   # If this is the equals button
        tk.Button(
            frame,                # Parent is the frame
            text=button,          # Button text
            width=5, height=2,    # Button size
            font=("Arial", 14),   # Font style
            command=calculate     # When clicked, run calculate()
        ).grid(row=row, column=col)  # Place button in the grid
    else:
        tk.Button(
            frame,                              # Parent is the frame
            text=button,                        # Button text
            width=5, height=2,                  # Button size
            font=("Arial", 14),                 # Font style
            command=lambda b=button: button_click(b)  # Insert that button's value
        ).grid(row=row, column=col)             # Place button in the grid

    col += 1  # Move to the next column
    if col > 3:  # After 4 columns, move to next row
        col = 0  # Reset column index
        row += 1 # Increase row index

# Create a "Clear" button below the grid
tk.Button(
    root,                   # Parent is the main window
    text="Clear",           # Button text
    font=("Arial", 14),     # Font style
    command=clear           # When clicked, clear the entry box
).pack(fill="x", padx=10, pady=10)  # Place it, fill horizontally with padding

# Start the Tkinter event loop (keeps the window open and responsive)
root.mainloop()
