import tkinter as tk

def show_prototype():
    root = tk.Tk()
    root.title("Inital Design - Defence Quiz")
    root.geometry("500x500")

    header = tk.Label(root, text="Security Classifications Quiz", font=("Arial", 16,))
    header.pack(pady=20)

    q_text = "What does OS stand for?"
    question_label = tk.Label(root, text=q_text, font=("Arial", 12))
    question_label.pack(pady=10)

    options = [
    "Select an answer...",
    "Official-Sensitive",
    "Official-Secret",
    "Operating-Software"
    ]

    selected_option = tk.StringVar(root)
    selected_option.set(options[0])

    dropdown = tk.OptionMenu(root, selected_option, *options)
    dropdown.pack(pady=20)

    submit_btn = tk.Button(root, text="Submit", width=15)
    submit_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_prototype()
