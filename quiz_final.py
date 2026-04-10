import tkinter as tk
from tkinter import messagebox
import random
import json
import os
from datetime import datetime

# ---------- FILE ----------
FILE = "scores.json"

# ✅ SAFE LOAD
if os.path.exists(FILE):
    try:
        with open(FILE, "r") as f:
            content = f.read().strip()
            if content:
                scores = json.loads(content)
            else:
                scores = []
    except:
        scores = []
else:
    scores = []

# ---------- DATA ----------
users = {"manoj": "123"}

admin = {
    "admin": "admin123",
    "superadmin": "1234"
}

quiz_data = {
    "Python": [
        {"q": "Who developed Python?", "options": ["Guido", "Elon", "Gates", "Jobs"], "ans": "Guido"},
        {"q": "Python is?", "options": ["Low-level", "High-level", "Machine", "None"], "ans": "High-level"}
    ]
}

root = tk.Tk()
root.title("Quiz System")
root.geometry("600x500")
root.configure(bg="#1e1e2f")

current_user = ""
questions = []
q_index = 0
score = 0

# ---------- SAVE ----------
def save_scores():
    try:
        with open(FILE, "w") as f:
            json.dump(scores, f, indent=4)
    except Exception as e:
        print("Error saving:", e)

# ---------- UI ----------
def clear():
    for w in root.winfo_children():
        w.destroy()

def title(text):
    tk.Label(root, text=text, font=("Arial", 20, "bold"),
             fg="white", bg="#1e1e2f").pack(pady=20)

def button(text, cmd):
    tk.Button(root, text=text, width=25, height=2,
              bg="#4CAF50", fg="white",
              command=cmd).pack(pady=10)

# ---------- MAIN ----------
def main_menu():
    clear()
    title("Quiz System")

    button("User Login", user_login)
    button("Register", register)
    button("Admin Login", admin_login)

# ---------- REGISTER ----------
def register():
    clear()
    title("Register")

    u = tk.Entry(root); u.pack(pady=5)
    p = tk.Entry(root, show="*"); p.pack(pady=5)

    def save():
        users[u.get()] = p.get()
        messagebox.showinfo("Success", "Registered!")
        main_menu()

    button("Submit", save)

# ---------- USER LOGIN ----------
def user_login():
    clear()
    title("User Login")

    u = tk.Entry(root); u.pack(pady=5)
    p = tk.Entry(root, show="*"); p.pack(pady=5)

    def login():
        global current_user
        if u.get() in users and users[u.get()] == p.get():
            current_user = u.get()
            user_menu()
        else:
            messagebox.showerror("Error", "Invalid")

    button("Login", login)

# ---------- USER MENU ----------
def user_menu():
    clear()
    title(f"Welcome {current_user}")

    topic_var = tk.StringVar()
    tk.OptionMenu(root, topic_var, *quiz_data.keys()).pack(pady=10)

    button("Start Quiz", lambda: start_quiz(topic_var.get()))

# ---------- QUIZ ----------
def start_quiz(topic):
    global questions, q_index, score

    if topic == "":
        messagebox.showerror("Error", "Select topic")
        return

    questions = quiz_data[topic][:]
    random.shuffle(questions)

    questions = questions[:5]

    q_index = 0
    score = 0

    show_question()

def show_question():
    clear()

    if q_index < len(questions):
        q = questions[q_index]

        title(f"Q{q_index+1}: {q['q']}")

        for opt in q["options"]:
            tk.Button(root, text=opt, width=30,
                      command=lambda o=opt: check(o)).pack(pady=5)
    else:
        save_score()

def check(ans):
    global score, q_index

    if ans == questions[q_index]["ans"]:
        score += 1

    q_index += 1
    show_question()

# ---------- SAVE SCORE ----------
def save_score():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    scores.append([current_user, score, date, time])
    save_scores()

    messagebox.showinfo("Saved", "Score saved permanently!")
    user_menu()

# ---------- ADMIN ----------
def admin_login():
    clear()
    title("Admin Login")

    u = tk.Entry(root); u.pack()
    p = tk.Entry(root, show="*"); p.pack()

    def login():
        if u.get() in admin and admin[u.get()] == p.get():
            admin_panel()
        else:
            messagebox.showerror("Error", "Invalid")

    button("Login", login)

def admin_panel():
    clear()
    title("Admin Panel")

    button("View Scores", view_scores)
    button("Add Topic", add_topic)
    button("Update Topic", update_topic)

# ---------- VIEW SCORES ----------
def view_scores():
    clear()
    title("User Scores")

    if not scores:
        tk.Label(root, text="No scores available",
                 fg="white", bg="#1e1e2f").pack()
    else:
        for s in scores:
            tk.Label(root,
                     text=f"{s[0]} | Score: {s[1]} | Date: {s[2]} | Time: {s[3]}",
                     fg="white", bg="#1e1e2f").pack()

    button("Back", admin_panel)

# ---------- ADD TOPIC ----------
def add_topic():
    clear()
    title("Enter Topic")

    topic_entry = tk.Entry(root)
    topic_entry.pack(pady=10)

    def next_step():
        topic = topic_entry.get()
        if topic == "":
            messagebox.showerror("Error", "Enter topic")
            return

        quiz_data[topic] = []
        add_questions(topic)

    button("Next", next_step)

# ---------- UPDATE TOPIC ----------
def update_topic():
    clear()
    title("Select Topic")

    topic_var = tk.StringVar()
    tk.OptionMenu(root, topic_var, *quiz_data.keys()).pack(pady=10)

    def next_step():
        topic = topic_var.get()
        if topic == "":
            messagebox.showerror("Error", "Select topic")
            return

        add_questions(topic)

    button("Next", next_step)

# ---------- ADD QUESTIONS ----------
def add_questions(topic):
    clear()
    title(f"Add Questions to {topic}")

    q_entry = tk.Entry(root)
    q_entry.pack(pady=5)

    opts = []
    for i in range(4):
        e = tk.Entry(root)
        e.pack(pady=2)
        opts.append(e)

    ans_entry = tk.Entry(root)
    ans_entry.pack(pady=5)

    def save_q():
        quiz_data[topic].append({
            "q": q_entry.get(),
            "options": [e.get() for e in opts],
            "ans": ans_entry.get()
        })

        messagebox.showinfo("Added", "Question Added")

        q_entry.delete(0, tk.END)
        for e in opts:
            e.delete(0, tk.END)
        ans_entry.delete(0, tk.END)

    button("Add Another Question", save_q)
    button("Finish", admin_panel)

# ---------- START ----------
main_menu()
root.mainloop()