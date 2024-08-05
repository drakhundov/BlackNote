import tkinter as tk
import conf


class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(conf.TITLE)
        self.window.iconbitmap(conf.ICON)
        self.main_menu = tk.Menu(self.window)
        self.options = tk.Menu(self.main_menu)
        self.window.configure(menu=self.main_menu)
        self.main_menu.add_cascade(label="File", menu=self.options)
        self.text = tk.Text(
            self.window, bg=conf.TEXT_BG, fg=conf.TEXT_FG, font=conf.TEXT_FONT
        )
        self.text.pack(side=tk.LEFT, fill=tk.BOTH)
        # TODO: add scrollbar

    def write_text(self, text):
        self.text.insert(1.0, text)

    def read_text(self):
        return self.text.get(1.0, tk.END)

    def reset_text(self):
        self.text.delete(1.0, tk.END)

    def update(self):
        self.window.update_idletasks()
        self.window.update()
