import tkinter as tk
from tkinter import ttk

# This simple class holds the state of the application
class TestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AuraPass 1.0")
        self.root.geometry("400x200")
        
        # Initialize a counter variable
        self.counter = 0

        # Style the root window using Tailwind-like classes (for conceptual clarity)
        self.root.configure(bg="#f0f0f0") 
        
        # Use a style for better button and label appearance (ttk is recommended)
        style = ttk.Style()
        style.configure('TLabel', font=('Inter', 14), background="#f0f0f0", foreground="#333333")
        style.configure('TButton', font=('Inter', 12, 'bold'), padding=10, background="#4CAF50", foreground="white")
        style.map('TButton', 
                 background=[('active', '#45A049')])

        # 1. Label to display text and updates
        self.message_var = tk.StringVar(value="Click the button to start the test.")
        
        self.message_label = ttk.Label(
            root, 
            textvariable=self.message_var, 
            style='TLabel'
        )
        self.message_label.pack(pady=30, padx=20)

        # 2. Button to trigger the update function
        self.test_button = ttk.Button(
            root, 
            text="Increment Counter & Test", 
            command=self.update_message,
            style='TButton'
        )
        self.test_button.pack(pady=10)

        # Center the window on the screen (optional but good practice)
        self.center_window()

    def update_message(self):
        """Increments the counter and updates the label text."""
        self.counter += 1
        new_text = f"Success! This executable works. Count: {self.counter}"
        self.message_var.set(new_text)

    def center_window(self):
        """Calculates and applies coordinates to center the window."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.root.geometry(f'{width}x{height}+{x}+{y}')


if __name__ == "__main__":
    # Initialize the main window
    root = tk.Tk()
    
    # Create an instance of the app
    app = TestApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()
# This simple class holds the state of the application