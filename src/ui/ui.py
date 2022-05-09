import tkinter as tk


from services.dictionary_service import EmptyItemError, dictionary_service
from services.game_service import game_service

bg_color = "#535459"
dark_color = "#36363b"
button_color = "#b5040c"


class AddWordsView:
    """The view where the player can add custom words to the dictionary."""

    def __init__(self, root, show_main_view):
        self.root = root
        self.buttons_frame = None
        self.textbox_frame = None
        self.show_main_view = show_main_view

        self.initialize()

    def pack(self):
        self.buttons_frame.pack()
        self.textbox_frame.pack()

    def destroy(self):
        self.buttons_frame.destroy()
        self.textbox_frame.destroy()

    def handle_add_word_button(self):
        word = self.word_entry.get()
        definitions_as_string = self.definition_box.get("1.0", "end-1c")
        try:
            dictionary_service.add_to_player_dictionary(word, definitions_as_string)
        except EmptyItemError as error:
            print(error)
        self.word_entry.delete(0, "end")
        self.definition_box.delete(1.0, "end")

    def initialize(self):
        self.buttons_frame = tk.Frame(master=self.root, background=dark_color)
        self.textbox_frame = tk.Frame(master=self.root, background=bg_color)
        self.add_word_button = tk.Button(
            master=self.buttons_frame,
            text="Add Word",
            command=self.handle_add_word_button,
            background=button_color,
        )
        self.word_entry = tk.Entry(master=self.buttons_frame)
        self.definition_box = tk.Text(master=self.textbox_frame, background=dark_color)
        change_view_button = tk.Button(
            master=self.buttons_frame,
            text="Back to Main View",
            command=self.show_main_view,
            background=button_color,
        )

        info_label = tk.Label(
            master=self.textbox_frame,
            text="Enter your word and its definitions below. Each definition on its own line. "
            "\nThe entries are saved in data/player_dictionary.xml",
            background=bg_color,
        )

        word_entry_text = tk.Label(
            master=self.buttons_frame, text="Word: ", fg="white", background=dark_color
        )

        change_view_button.grid(row=0, column=1)
        word_entry_text.grid(row=1, column=0)
        self.word_entry.grid(row=1, column=1)
        self.add_word_button.grid(row=1, column=2)
        info_label.pack()
        self.definition_box.pack()


class MainView:
    """The main view where the player can guess words. Opened when the program first starts."""

    def __init__(self, root, show_add_words_view) -> None:
        self.root = root
        self.show_add_words_view = show_add_words_view
        self.answer_frame = None
        self.textbox_frame = None
        self.textbox = None

        self.initialize()

    def destroy(self):
        self.answer_frame.destroy()
        self.textbox_frame.destroy()

    def pack(self):
        self.answer_frame.pack(pady=(0, 25))
        self.textbox_frame.pack(fill="both")

    def update_labels(self):
        self.attempts_label.config(text=f"Attempts: {game_service.get_attempts()}")
        total_points = game_service.get_total_points()
        points_to_gain = game_service.get_points_to_gain()
        self.total_points_label.config(text=f"Points: {total_points}")
        self.points_to_gain_label.config(text=f"Points to gain: {points_to_gain}")

    def handle_submit_button(self, answer: str):
        state = self.submit_button["state"]
        if str(state) == "disabled":
            return
        result = game_service.check_answer(answer)
        if result is True:
            self.insert_to_textbox(f"Correct! The word was {answer}.")
            self.insert_to_textbox(f"+{game_service.get_points_to_gain()} points")
            self.submit_button.config(state="disabled")
            self.hint_button.config(state="disabled")
        else:
            self.insert_to_textbox("Wrong, try again! (-1 points)")
        self.update_labels()

    def handle_new_word_button(self, *, category):
        item = game_service.new_item(category=category)
        if not item:
            self.insert_to_textbox(
                "Could not get item, your player_dictionary.xml file might be empty!"
            )
            return
        definitions = game_service.get_readable_definitions()
        self.clear_textbox()
        self.answer_entry.delete(0, "end")
        self.insert_to_textbox(
            f"Guess the following {game_service.get_word_length()} letter word: "
        )
        for defn in definitions:
            self.insert_to_textbox(defn)
        self.insert_to_textbox(
            "You can press the hint button to get hints, "
            "but it will decrease the amount of points you gain."
        )
        self.submit_button.config(state="normal")
        self.hint_button.config(state="normal")
        self.update_labels()

    def handle_hint_button(self):
        game_service.reveal_next_letter()
        self.insert_to_textbox(f"Hint: {game_service.get_readable_underscores()}")
        self.update_labels()

    def clear_textbox(self):
        self.textbox.config(state="normal")
        self.textbox.delete(1.0, "end")
        self.textbox.config(state="disabled")

    def insert_to_textbox(self, line):
        self.textbox.config(state="normal")
        self.textbox.insert("end", line + "\n")
        self.textbox.config(state="disabled")
        self.textbox.see("end")

    def initialize(self):
        self.answer_frame = tk.Frame(
            master=self.root,
            highlightbackground=bg_color,
            highlightthickness=1,
            background=dark_color,
        )
        self.answer_frame.bind()
        self.root.bind(
            "<Return>", lambda x: self.handle_submit_button(self.answer_entry.get())
        )
        self.textbox_frame = tk.Frame(master=self.root, background=dark_color)
        self.textbox = tk.Text(master=self.textbox_frame, background=dark_color)

        answer_label = tk.Label(
            master=self.textbox_frame, text="The word is: ", background=dark_color
        )
        self.total_points_label = tk.Label(master=self.answer_frame, text="Points: 0")
        self.points_to_gain_label = tk.Label(
            master=self.answer_frame, text="Points to gain: 0"
        )
        self.attempts_label = tk.Label(master=self.answer_frame)

        self.answer_entry = tk.Entry(master=self.textbox_frame)
        new_word_button = tk.Button(
            master=self.answer_frame,
            text="New Word",
            command=lambda: self.handle_new_word_button(category="main"),
            background=button_color,
        )
        new_custom_word_button = tk.Button(
            master=self.answer_frame,
            text="New Custom Word",
            command=lambda: self.handle_new_word_button(category="custom"),
            background=button_color,
        )
        self.hint_button = tk.Button(
            master=self.answer_frame,
            text="Hint (-1)",
            command=self.handle_hint_button,
            background=button_color,
        )
        self.submit_button = tk.Button(
            master=self.answer_frame,
            text="Submit (ENTER)",
            command=lambda: self.handle_submit_button(self.answer_entry.get()),
            background=button_color,
        )
        change_view_button = tk.Button(
            master=self.answer_frame,
            text="Add Custom Words",
            command=self.show_add_words_view,
            bg=button_color,
        )

        self.submit_button.grid(row=0, column=0)
        new_word_button.grid(row=0, column=1)
        new_custom_word_button.grid(row=0, column=2)
        self.hint_button.grid(row=0, column=3)
        change_view_button.grid(row=0, column=4)

        self.total_points_label.grid(row=1, column=0)
        self.attempts_label.grid(row=1, column=1)
        self.points_to_gain_label.grid(row=1, column=3)

        answer_label.pack()
        self.answer_entry.pack()
        self.textbox.pack(fill="both")

        definitions = game_service.get_readable_definitions()
        self.insert_to_textbox(
            f"Guess the following {game_service.get_word_length()} letter word: "
        )
        for defn in definitions:
            self.insert_to_textbox(defn)
        self.insert_to_textbox(
            "You can press the hint button to get hints, "
            "but it will decrease the amount of points you gain."
        )
        self.update_labels()


class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def show_main_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = MainView(self.root, self.show_add_words_view)
        self.current_view.pack()

    def show_add_words_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = AddWordsView(self.root, self.show_main_view)
        self.current_view.pack()

    def start(self):
        self.show_main_view()
