import tkinter as tk
from tkinter import messagebox
from logic import validate_name

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Classification Quiz")
        self.root.geometry("500x500")

        self.user_name = ""

        self.setup_welcome_screen()

    def setup_welcome_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Security Classification Quiz", font=("Arial", 16)).pack(pady=30)

        tk.Label(self.root, text="Enter Full Name:").pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=10)

        start_btn = tk.Button(self.root, text="Start", command=self.handle_start)
        start_btn.pack(pady=20)

    def handle_start(self):
        input_name = self.name_entry.get()

        if validate_name(input_name):
            self.user_name = input_name
            self.setup_question_screen()
        else:
            messagebox.showwarning("Please enter a valid name")

    def setup_question_screen(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Employee: {self.user_name}", fg="light blue").pack(padx=10)
                 
        q_text = "What does OS stand for?"
        tk.Label(self.root, text=q_text, font=("Arial", 12), wraplength=450).pack(pady=20) 

        self.options = ["Select an answer...", "Official-Secret", "Official-Sensitive", "Operating-Software"]
        self.selection = tk.StringVar(self.root)
        self.selection.set(self.options[0])

        self.menu = tk.OptionMenu(self.root, self.selection, *self.options)
        self.menu.pack(pady=20)

        submit_btn = tk.Button(self.root, text="Next", command=lambda: print("Next"))
        submit_btn.pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


      
