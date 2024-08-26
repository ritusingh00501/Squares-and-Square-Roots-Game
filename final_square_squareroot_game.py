import tkinter as tk
from tkinter import messagebox
import random
import math 
import time
import threading 

root = tk.Tk()
root.geometry("500x600")
root.title("Squares and Square Roots Game")
root.config(background="#66ffff")

def is_perfect_square(n):
    return math.isqrt(n)**2==n

def display_processing_bar():
    for _ in range(10):
        time.sleep(0.2)
        progress_label.config(text=progress_label.cget("text")+".")
        root.update()
    progress_label.config(text="")
    
def ask_square_question():
    num = random.randint(1,100)
    correct_answer = num**2
    question_label.config(text=f"What is the Square of {num}?")
    return correct_answer

def ask_square_root_question():
    num = random.randint(1,10000)
    while not is_perfect_square(num):
        num = random.randint(1,10000)
    correct_answer = int(math.sqrt(num))
    question_label.config(text=f"What is Square root of {num}?")
    return correct_answer

def start_game():
    global player_name, correct_answer, consecutive_correct
    player_name = name_entry.get()
    if not player_name:
        messagebox.showerror("Invalid input","Please enter your name.")
        return 
    #question_label.config(text=f"Ready, {player_name}? Your question will appear here.")
    name_entry.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)
    answer_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)
    #print(f"Game started for {name_entry.get()}!")
    
    consecutive_correct = 0
    continue_game()
    
def continue_game():
    global correct_answer
    answer_entry.delete(0,tk.END)
    question_type = random.choice(["square","square_root"])
    if question_type == "square":
        correct_answer = ask_square_question()
    else:
        correct_answer = ask_square_root_question()
      
def check_answer():
    global consecutive_correct, correct_answer
    try:
        player_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input","Please enter a valid number.")
        return 
    
    threading.Thread(target=display_processing_bar).start()
    time.sleep(2) #Give time for the processing bar to finish 
    
    if player_answer == correct_answer:
        result_label.config(text="Correct!")
        consecutive_correct += 1
    else:
        result_label.config(text="Incorrect!")
        consecutive_correct = 0
        
    if consecutive_correct == 3:
        messagebox.showinfo("Winner!",f"Congratulations {player_name}, you are the winner!")
        root.quit()
    else:
        continue_game()
       
def quit_game():
    messagebox.showinfo("Game Over",f"Game over! {player_name}, you are declared a loser.")
    root.quit()
    
frame=tk.Frame(root,relief="solid",bd=1,bg="#ccffcc")
frame.pack(fill="both",expand=True,padx=100,pady=100)    
tk.Label(frame, text="Welcom to the Squares and Square Root Game!", font=("arial",20)).pack(pady=10)
tk.Label(frame, text="Please Enter Your Name : ", font=("arial",15)).pack(pady=5)
name_entry = tk.Entry(frame)
name_entry.pack(pady=5)

start_button = tk.Button(frame,text="Start Game", command=start_game, fg="red",bg="yellow",font="arial")
start_button.pack(pady=10)

question_label = tk.Label(frame, text="", font=("Helvetica",14))
question_label.pack(pady=10)

tk.Label(frame,text="Your answer: ").pack(pady=5)
answer_entry = tk.Entry(frame, state=tk.DISABLED)
answer_entry.pack(pady=5)

#answer_entry=tk.Entry(frame,state=tk.DISABLED)
#answer_entry.pack(pack=5)

submit_button = tk.Button(frame, text="Submit answer",state=tk.DISABLED,command=check_answer, font=("Helvetica",14),fg="Black",bg="pink")
submit_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Helvetica",14))
result_label.pack(pady=10)

progress_label = tk.Label(frame, text="", font=("Helvetica",14))
progress_label.pack(pady=10)

quit_button = tk.Button(frame, text="Quit Game",command=quit_game, font=("Helvetica",14),fg="Black",bg="orange")
quit_button.pack(pady=10)

player_name = ""
consecutive_correct = 0
correct_answer = 0

root.mainloop()
