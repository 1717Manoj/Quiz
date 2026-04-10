import tkinter as tk
from tkinter import messagebox
import random, json, os
from datetime import datetime

FILE = "scores.json"

# ---------- SAFE LOAD ----------
def load_scores():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except:
        pass
    return []

scores = load_scores()

# ---------- SAVE ----------
def save_scores():
    with open(FILE, "w") as f:
        json.dump(scores, f, indent=4)

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

# ---------- APP ----------
root = tk.Tk()
root.title("Quiz Pro System")
root.geometry("700x520")
root.configure(bg="#121212")

current_user = ""
questions = []
q_index = 0
score = 0

# ---------- UI ----------
def clear():
    for w in root.winfo_children():
        w.destroy()

def header(text):
    tk.Label(root, text=text, font=("Arial", 22, "bold"),
             fg="white", bg="#121212").pack(pady=15)

def button(text, cmd, color="#4CAF50"):
    tk.Button(root, text=text, width=25, height=2,
              bg=color, fg="white", command=cmd).pack(pady=6)

# ---------- MAIN ----------
def main_menu():
    clear()
    header("Quiz Pro System")

    button("User Login", user_login)
    button("Register", register)
    button("Admin Login", admin_login)

# ---------- REGISTER ----------
def register():
    clear()
    header("Register")

    u = tk.Entry(root); u.pack(pady=5)
    p = tk.Entry(root, show="*"); p.pack(pady=5)

    def save():
        users[u.get()] = p.get()
        messagebox.showinfo("Success", "Registered")
        main_menu()

    button("Submit", save)
    button("Back", main_menu, "#f44336")

# ---------- USER LOGIN ----------
def user_login():
    clear()
    header("User Login")

    u = tk.Entry(root); u.pack(pady=5)
    p = tk.Entry(root, show="*"); p.pack(pady=5)

    def login():
        global current_user
        if u.get() in users and users[u.get()] == p.get():
            current_user = u.get()
            user_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    button("Login", login)
    button("Back", main_menu, "#f44336")

# ---------- USER MENU ----------
def user_menu():
    clear()
    header(f"Welcome {current_user}")

    topic = tk.StringVar()
    tk.OptionMenu(root, topic, *quiz_data.keys()).pack(pady=10)

    button("Start Quiz", lambda: start_quiz(topic.get()))
    button("Logout", main_menu, "#f44336")

# ---------- QUIZ ----------
def start_quiz(topic):
    global questions, q_index, score

    if topic == "":
        messagebox.showerror("Error", "Select topic")
        return

    questions = quiz_data[topic][:]
    random.shuffle(questions)

    q_index = 0
    score = 0

    show_q()

def show_q():
    clear()

    if q_index < len(questions):
        q = questions[q_index]

        header(f"Q{q_index+1}/{len(questions)}")

        tk.Label(root, text=q["q"], fg="white",
                 bg="#121212", font=("Arial", 14)).pack(pady=10)

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
    show_q()

# ---------- SAVE SCORE (HIDDEN FROM USER) ----------
def save_score():
    now = datetime.now()

    scores.append({
        "user": current_user,
        "score": score,
        "total": len(questions),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S")
    })

    save_scores()

    messagebox.showinfo("Completed", "Quiz Completed Successfully!")
    user_menu()

# ---------- ADMIN ----------
def admin_login():
    clear()
    header("Admin Login")

    u = tk.Entry(root); u.pack()
    p = tk.Entry(root, show="*"); p.pack()

    def login():
        if u.get() in admin and admin[u.get()] == p.get():
            admin_panel()
        else:
            messagebox.showerror("Error", "Invalid")

    button("Login", login)
    button("Back", main_menu, "#f44336")

def admin_panel():
    clear()
    header("Admin Dashboard")

    button("View Scores", view_scores)
    button("Add Topic", add_topic)
    button("Update Topic", update_topic)
    button("Delete Topic", delete_topic)
    button("Delete Question", delete_question)
    button("Clear Scores", clear_scores)
    button("Logout", main_menu, "#f44336")

# ---------- VIEW SCORES ----------
def view_scores():
    clear()
    header("All Scores")

    if not scores:
        tk.Label(root, text="No Data", fg="white", bg="#121212").pack()
    else:
        for s in scores:
            tk.Label(root,
                text=f"{s['user']} | {s['score']}/{s['total']} | {s['date']} {s['time']}",
                fg="white", bg="#121212").pack()

    button("Back", admin_panel)

# ---------- ADD / UPDATE ----------
def add_topic():
    clear()
    header("Add Topic")

    topic = tk.Entry(root)
    topic.pack()

    button("Next", lambda: add_questions(topic.get()))

def update_topic():
    clear()
    header("Update Topic")

    topic = tk.StringVar()
    tk.OptionMenu(root, topic, *quiz_data.keys()).pack()

    button("Next", lambda: add_questions(topic.get()))

def add_questions(topic):
    clear()
    header(topic)

    q = tk.Entry(root); q.pack()

    opts = []
    for i in range(4):
        e = tk.Entry(root)
        e.pack()
        opts.append(e)

    ans = tk.Entry(root); ans.pack()

    def save():
        if topic not in quiz_data:
            quiz_data[topic] = []

        quiz_data[topic].append({
            "q": q.get(),
            "options": [e.get() for e in opts],
            "ans": ans.get()
        })

        messagebox.showinfo("Added", "Question Added")

    button("Add More", save)
    button("Done", admin_panel)

# ---------- DELETE ----------
def delete_topic():
    clear()
    header("Delete Topic")

    topic = tk.StringVar()
    tk.OptionMenu(root, topic, *quiz_data.keys()).pack()

    def delete():
        if topic.get() in quiz_data:
            del quiz_data[topic.get()]
            messagebox.showinfo("Done", "Deleted")
            admin_panel()

    button("Delete", delete)

def delete_question():
    clear()
    header("Delete Question")

    topic = tk.StringVar()
    tk.OptionMenu(root, topic, *quiz_data.keys()).pack()

    def next():
        t = topic.get()
        clear()

        for i, q in enumerate(quiz_data[t]):
            tk.Button(root, text=q["q"],
                      command=lambda i=i: remove_q(t, i)).pack()

    button("Next", next)

def remove_q(topic, index):
    del quiz_data[topic][index]
    messagebox.showinfo("Done", "Deleted")
    admin_panel()

# ---------- CLEAR ----------
def clear_scores():
    scores.clear()
    save_scores()
    messagebox.showinfo("Done", "Scores Cleared")
    admin_panel()

# ---------- START ----------
main_menu()
root.mainloop()