import tkinter as tk
from tkinter import messagebox
import csv
import os
from logic import validate_name

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Classification Quiz")
        self.root.geometry("500x500")

        self.user_name = ""
        self.questions = []
        self.current_question_index = 0
        self.score = 0

        self.load_questions()

        self.setup_welcome_screen()

    def load_questions(self):
        file_path = os.path.join("data", "quiz_data.csv")
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.questions = list(reader)
        except FileNotFoundError:
            messagebox.showerror("Data Error", "quiz_data.csv not found in data/ folder.") 

    def setup_welcome_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Security Classification Quiz", font=("Arial", 16)).pack(pady=30)

        tk.Label(self.root, text="Please Enter Full Name:").pack()

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
        q_data = self.questions[self.current_question_index]

        tk.Label(self.root, text=f"Employee: {self.user_name}", fg="light blue").pack(padx=10)
        tk.Label(self.root, text=f"Question {self.current_question_index + 1}", font=("Arial", 12, "bold")).pack(pady=5)

        tk.Label(self.root, text=q_data['Question'], font=("Arial", 12), wraplength=450).pack(pady=20) 

        self.options = [q_data['OptionA'], q_data['OptionB'], q_data['OptionC']]
        self.selection = tk.StringVar(self.root)
        self.selection.set("Choose an answer...")

        tk.OptionMenu(self.root, self.selection, *self.options).pack(pady=20)

        tk.Button(self.root, text="Submit", command=self.handle_submit).pack(pady=20)

    def handle_submit(self):
        user_choice = self.selection.get()
        if user_choice == "Choose an answer...":
            messagebox.showwarning("No Selection, please choose an answer")
            return
        
        q_data = self.questions[self.current_question_index]
        correct_letter = q_data['CorrectAnswer']
        mapping = {'A': 'OptionA', 'B': 'OptionB', 'C': 'OptionC'}
        correct_text = q_data[mapping[correct_letter]]

        if user_choice == correct_text:
            self.score += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.setup_question_screen()
        else:
            self.show_results()

    def show_results(self):
        self.clear_screen()
        tk.Label(self.root, text="Quiz Complete, Thank you!", font=("Arial", 16, "italic")).pack(pady=30)
        tk.Label(self.root, text=f"Employee: {self.user_name}").pack()
        tk.Label(self.root, text=f"Final Score: {self.score} / {len(self.questions)}", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="Finish", command=self.root.quit).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()             

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


      
