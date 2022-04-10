from tkinter import Tk, ttk, constants
from services.game_service import *


class UI:
    def __init__(self, root):
        self.root = root
        self.answer_entry = None

    def start(self):
        answer_label = ttk.Label(master=self.root, text="The word is: ")
        self.answer_entry = ttk.Entry(master=self.root)

        submit_button = ttk.Button(master=self.root, text="Submit", command=lambda: self.handle_submit_button_click())

        answer_label.grid(row=0, column=0)
        self.answer_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=0, columnspan=2)

    def handle_submit_button_click(self):
        answer = self.answer_entry.get()
        print(answer)


window = Tk()
window.title("Dictionary Game")

ui = UI(window)
ui.start()

window.mainloop()
