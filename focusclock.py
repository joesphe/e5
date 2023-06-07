import time
import tkinter as tk

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=timer)
        time_label.update()
        time.sleep(1)
        t -= 1
    time_label.config(text='Time is up!')

def start_timer():
    minutes = int(minute_entry.get())
    seconds = minutes * 60
    countdown(seconds)

# 创建主窗口
root = tk.Tk()
root.title('Pomodoro Timer')

# 创建标签和输入框
time_label = tk.Label(root, text='00:00', font=('Helvetica', 48))
time_label.pack(pady=10)
minute_entry = tk.Entry(root, width=10, font=('Helvetica', 24))
minute_entry.insert(0, '25')
minute_entry.pack(pady=10)

# 创建按钮
start_button = tk.Button(root, text='Start', command=start_timer)
start_button.pack(pady=10)

root.mainloop()
