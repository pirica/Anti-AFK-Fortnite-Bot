import tkinter as tk
import pyautogui
import time
import threading
from tkinter import messagebox

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required libraries
try:
    import tkinter as tk
    import pyautogui
except ImportError:
    install('tkinter')
    install('pyautogui')
    import tkinter as tk
    import pyautogui

class App:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg='#00bfff', width=500, height=500)

        # Add a title label
        self.title = tk.Label(self.frame, text='AFK Presser', font=('Helvetica', 30, 'bold'), bg='#00bfff', fg='white')
        self.title.pack(pady=(20, 0))

        # Add the start and close buttons
        self.button1 = tk.Button(self.frame, text='Start', width=25, bg='#FF0000', font=('Helvetica', 20, 'bold'), command=self.start)
        self.button1.pack(pady=(20, 10))
        self.button2 = tk.Button(self.frame, text='Close', width=25, bg='#00FF00', font=('Helvetica', 20, 'bold'), command=self.close)
        self.button2.pack(pady=(0, 20))
        self.frame.pack()

        # Add a flag to keep track of whether the loop is running
        self.running = False
        self.stop_thread = False
        self.paused = False

    def start(self):
        if self.running:
            # If the loop is already running, pause it
            if self.paused:
                # If the loop is paused, resume it
                self.paused = False
                self.button1.config(text='Pause')
            else:
                # If the loop is not paused, pause it
                self.paused = True
                self.button1.config(text='Resume')
        else:
            # If the loop is not running, start it
            self.running = True
            self.stop_thread = False
            self.button1.config(text='Pause')

            # Create a new thread to run the loop
            self.thread = threading.Thread(target=self.loop)
            self.thread.start()

    def loop(self):
        # Set the timer to 120 seconds
        timer = 1

        # Run the loop until the stop_thread flag is set to True
        while not self.stop_thread:
            # If the loop is paused, sleep for a short time before checking the paused flag again
            while self.paused:
                time.sleep(0.1)
            pyautogui.press('w')
            time.sleep(timer)
            pyautogui.press('s')
            time.sleep(timer)

    def close(self):
        # Set the running flag to False to stop the loop
        self.stop_thread = True
        self.running = False
        self.paused = False
        self.button1.config(text='Start')
        self.master.destroy()

root = tk.Tk()
root.title("AFK Presser")
root.configure(bg='#00bfff', width=500, height=500)
app = App(root)

# Display critical message
messagebox.showerror("Made by Albuman", "The stop button aint work so just close the application. Btw you might need 2 use task manager")

root.mainloop()


