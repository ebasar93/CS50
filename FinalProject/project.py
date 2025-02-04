import tkinter as tk
from tkinter import messagebox
import random

# Global variable to control the timer's state
timer_running = False
time_left = 0

def main():
    root.mainloop()

def countdown():
    global time_left
    if time_left > 0 and timer_running:
        mins, secs = divmod(time_left, 60)
        time_str = "{:02d}:{:02d}".format(mins, secs)
        label.config(text=time_str)
        time_left -= 1
        root.after(1000, countdown)
    elif time_left == 0 and timer_running:
        if random.choice([True, False]):
            messagebox.showinfo("Timer", "Restarting timer")
            start_timer()
        else:
            label.config(text="Time's up!")
            messagebox.showinfo("Timer", "Time's up!")

def start_timer():
    global timer_running, time_left
    if not timer_running:
        timer_running = True
        try:
            time_left = int(entry.get()) * 60
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
        countdown()

def pause_resume_timer():
    global timer_running
    timer_running = not timer_running
    if timer_running:
        countdown()

def reset_timer():
    global timer_running, time_left
    timer_running = False
    time_left = 0
    label.config(text="00:00")

root = tk.Tk()
root.title("Countdown Timer")

# Calculate the center position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 200
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Set the window background color
root.configure(bg='light blue')

label = tk.Label(root, font=("Courier", 44), fg="red", bg='light blue')
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

pause_resume_button = tk.Button(root, text="Pause/Resume", command=pause_resume_timer)
pause_resume_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_timer)
reset_button.pack()


if __name__ == "__main__":
    main()
