import tkinter
from tkinter import Tk, ttk, constants
from services.game_service import game_service


class MainView:
    def __init__(self, root) -> None:
        self.root = root
        self.frame = None
        self.textbox = None

        self.initialize()

    def pack(self):
        self.answer_frame.pack()
        self.definitions_frame.pack(fill="both")

    def handle_submit_button_click(self, answer: str):
        result = game_service.check_answer(answer)
        if result is True:
            self.insert_to_textbox(f"Correct! The word was {answer}.")
        else:
            self.insert_to_textbox(f"Wrong, try again!")

    def handle_new_word_button_click(self):
        game_service.new_item()
        definitions = game_service.get_readable_definitions()
        self.clear_textbox()
        self.underscores_label.config(text=game_service.get_readable_underscores())
        self.insert_to_textbox(f"Guess the following {game_service.get_word_length()} letter word: ")
        for defn in definitions:
            self.insert_to_textbox(defn)

    def handle_hint_button_click(self):
        game_service.reveal_next_letter()
        self.underscores_label.config(text=game_service.get_readable_underscores())

    def clear_textbox(self):
        self.textbox.config(state="normal")
        self.textbox.delete(1.0, constants.END)
        self.textbox.config(state="disabled")

    def insert_to_textbox(self, line):
        self.textbox.config(state="normal")
        self.textbox.insert(constants.END, line + "\n")
        self.textbox.config(state="disabled")

    def initialize(self):
        self.answer_frame = ttk.Frame(master=self.root)
        self.definitions_frame = ttk.Frame(master=self.root)
        self.textbox = tkinter.Text(master=self.definitions_frame)

        self.underscores_label = ttk.Label(master=self.answer_frame)
        answer_label = ttk.Label(master=self.answer_frame, text="The word is: ")
        answer_entry = ttk.Entry(master=self.answer_frame)
        new_word_button = ttk.Button(master=self.answer_frame, text="New Word", command=lambda: self.handle_new_word_button_click())
        hint_button = ttk.Button(master=self.answer_frame, text="Hint", command=lambda: self.handle_hint_button_click())
        submit_button = ttk.Button(
            master=self.answer_frame,
            text="Submit",
            command=lambda: self.handle_submit_button_click(answer_entry.get()),
        )

        self.underscores_label.grid(row=2, column=0)
        answer_label.grid(row=0, column=0)
        answer_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=0)
        new_word_button.grid(row=1, column=1)
        hint_button.grid(row=1, column=2)
        self.textbox.pack(fill="both")

        definitions = game_service.get_readable_definitions()
        self.underscores_label.config(text=game_service.get_readable_underscores())
        self.insert_to_textbox(f"Guess the following {game_service.get_word_length()} letter word: ")
        for defn in definitions:
            self.insert_to_textbox(defn)


class UI:
    def __init__(self, root):
        self.root = root

    def show_main_view(self):
        joku = MainView(self.root)
        joku.pack()

    def start(self):
        self.show_main_view()
