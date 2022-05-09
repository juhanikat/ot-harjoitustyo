from tkinter import Tk

from ui.ui import UI

window = Tk()
window.minsize(900, 600)
window.title("Dictionary Game")
window.config(bg="#535459")

ui = UI(window)
ui.start()

window.mainloop()
