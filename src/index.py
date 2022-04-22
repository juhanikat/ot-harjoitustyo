from tkinter import Tk

from ui.ui import UI

window = Tk()
window.title("Dictionary Game")

ui = UI(window)
ui.start()

window.mainloop()