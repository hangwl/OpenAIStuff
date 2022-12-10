#!/usr/bin/env python

import tkinter as tk
import time

class Stopwatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stopwatch")

        self.time_label = tk.Label(self.root, text="00:00:00")
        self.time_label.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.is_running = False
        self.current_time = 0
        self.elapsed_time = 0

        self.root.mainloop()

    def start(self):
        self.is_running = True
        self.current_time = time.time()

        self.start_time = time.time()
        self.update_time()

    def stop(self):
        self.is_running = False

    def reset(self):
        self.is_running = False
        self.current_time = 0
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

    def update_time(self):
        if self.is_running:
            self.elapsed_time = int(time.time() - self.start_time)
            minutes, seconds = divmod(self.elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)

            time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.time_label.config(text=time_string)

            self.root.after(10, self.update_time)

if __name__ == "__main__":
    app = Stopwatch()
