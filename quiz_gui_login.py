
import tkinter as tk
from tkinter import messagebox
import random

# Credentials
USER_CREDENTIALS = {"manoj": "123"}
ADMIN_CREDENTIALS = {"admin": "admin123"}

# Quiz Data
quiz_data = {
    "Python": [
        {"q": "Who developed Python?", "options": ["Guido", "Elon", "Gates", "Jobs"], "ans": "Guido"},
    ],
    "Java": [
        {"q": "Java developed by?", "options": ["Sun Microsystems", "Microsoft", "Apple", "IBM"], "ans": "Sun Microsystems"},
    ]
}

root = tk.Tk()
root.title("Quiz System")
root.geometry("400x400")

questions = []
q_index = 0
score = 0

# 🔄 Clear screen
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# 🎯 FIRST SCREEN (Choose Login Type)
def main_menu():
    clear_screen()

    tk.Label(root, text="Quiz System", font=("Arial", 18)).pack(pady=20)

    tk.Button(root, text="User Login", width=20, command=user_login).pack(pady=10)
    tk.Button(root, text="Admin Login", width=20, command=admin_login).pack(pady=10)

# 👤 USER LOGIN
def user_login():
    clear_screen()

    tk.Label(root, text="User Login", font=("Arial", 16)).pack(pady=10)

    username = tk.Entry(root)
    username.pack()
    password = tk.Entry(root, show="*")
    password.pack()

    def login():
        if username.get() in USER_CREDENTIALS and USER_CREDENTIALS[username.get()] == password.get():
            user_menu()
        else:
            messagebox.showerror("Error", "Invalid User Login")

    tk.Button(root, text="Login", command=login).pack(pady=10)

# 🔐 ADMIN LOGIN
def admin_login():
    clear_screen()

    tk.Label(root, text="Admin Login", font=("Arial", 16)).pack(pady=10)

    username = tk.Entry(root)
    username.pack()
    password = tk.Entry(root, show="*")
    password.pack()

    def login():
        if username.get() in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[username.get()] == password.get():
            admin_panel()
        else:
            messagebox.showerror("Error", "Invalid Admin Login")

    tk.Button(root, text="Login", command=login).pack(pady=10)

# 👤 USER MENU
def user_menu():
    clear_screen()

    tk.Label(root, text="Select Topic").pack(pady=10)

    topic_var = tk.StringVar()
    tk.OptionMenu(root, topic_var, *quiz_data.keys()).pack()

    def start_quiz():
        global questions, q_index, score
        topic = topic_var.get()

        if topic == "":
            messagebox.showerror("Error", "Select topic")
            return

        questions = quiz_data[topic]
        random.shuffle(questions)
        q_index = 0
        score = 0
        show_question()

    tk.Button(root, text="Start Quiz", command=start_quiz).pack(pady=10)

# ❓ QUESTIONS
def show_question():
    clear_screen()

    global q_index

    if q_index < len(questions):
        q = questions[q_index]

        tk.Label(root, text=q["q"]).pack(pady=10)

        for opt in q["options"]:
            tk.Button(root, text=opt,
                      command=lambda o=opt: check_answer(o)).pack(pady=5)
    else:
        messagebox.showinfo("Result", f"Score: {score}/{len(questions)}")
        main_menu()

# ✔ CHECK ANSWER
def check_answer(ans):
    global q_index, score

    if ans == questions[q_index]["ans"]:
        score += 1

    q_index += 1
    show_question()

# 🛠 ADMIN PANEL
def admin_panel():
    clear_screen()

    tk.Label(root, text="Admin Panel").pack(pady=10)

    topic = tk.Entry(root)
    topic.pack()
    topic.insert(0, "Topic")

    question = tk.Entry(root)
    question.pack()
    question.insert(0, "Question")

    options = []
    for i in range(4):
        e = tk.Entry(root)
        e.pack()
        e.insert(0, f"Option {i+1}")
        options.append(e)

    answer = tk.Entry(root)
    answer.pack()
    answer.insert(0, "Correct Answer")

    def add_q():
        t = topic.get()
        if t not in quiz_data:
            quiz_data[t] = []

        quiz_data[t].append({
            "q": question.get(),
            "options": [e.get() for e in options],
            "ans": answer.get()
        })

        messagebox.showinfo("Success", "Question Added")

    tk.Button(root, text="Add Question", command=add_q).pack(pady=10)

# ▶ Start
main_menu()
root.mainloop()