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

    def handle_submit_button_click(self):
        answer = self.answer_entry.get()
        result = game_service.check_answer(answer)
        if result is True:
            print("joo")

    def handle_new_word_button_click(self):
        game_service.new_item()
        definitions = game_service.get_readable_definitions()
        self.create_definition_list(definitions)

    def create_definition_list(self, definitions: list):
        self.textbox.config(state="normal")
        self.textbox.delete(1.0, constants.END)
        self.textbox.insert(constants.END, f"Guess the following {game_service.get_word_length()} letter word: \n")
        for defn in definitions:
            self.textbox.insert(constants.END, defn)
        self.textbox.config(state="disabled")

    def initialize(self):
        self.answer_frame = ttk.Frame(master=self.root)
        self.definitions_frame = ttk.Frame(master=self.root)
        self.textbox = tkinter.Text(master=self.definitions_frame)

        answer_label = ttk.Label(master=self.answer_frame, text="The word is: ")
        self.answer_entry = ttk.Entry(master=self.answer_frame)
        new_word_button = ttk.Button(master=self.answer_frame, text="New Word", command=lambda: self.handle_new_word_button_click())
        submit_button = ttk.Button(
            master=self.answer_frame,
            text="Submit",
            command=lambda: self.handle_submit_button_click(),
        )

        answer_label.grid(row=0, column=0)
        self.answer_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=0)
        new_word_button.grid(row=1, column=1)
        self.textbox.pack(fill="both")


class UI:
    def __init__(self, root):
        self.root = root

    def show_main_view(self):
        joku = MainView(self.root)
        joku.pack()

    def start(self):
        self.show_main_view()
