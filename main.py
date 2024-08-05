import sys
from tkinter import filedialog, messagebox

from ui import UI


class Main:
    def __init__(self):
        self.ui = UI()
        self.path = str()
        self.filetypes = [(".py files", "*.py"), (".txt files", "*.txt")]
        self.file_saved = False
        self.ui.options.add_command(label="Save File", command=self.save_file)
        self.ui.options.add_command(label="Open File", command=self.open_file)
        self.ui.options.add_command(
            label="Save As", command=lambda: self.save_file(new_path=True)
        )
        self.ui.options.add_command(label="New File", command=self.new_file)

    def save_file(self, new_path=False):
        try:
            if not self.path or new_path:
                path = filedialog.asksaveasfilename(
                    initialdir="/", title="Save File", filetypes=self.filetypes
                )
                self.path = path
                file_saved = True
            with open(self.path, "w") as file:
                file.write(self.ui.read_text())
        except:
            return

    def open_file(self):
        try:
            path = filedialog.askopenfilename(
                initialdir="/", title="Select File", filetypes=self.filetypes
            )
            self.path = path
            with open(self.path, "r") as file:
                self.ui.reset_text()
                self.ui.write_text(file.read())
        except:
            return

    def new_file(self):
        if not self.file_saved and messagebox.askyesno(
            title="You Haven't Saved Current File", message="Save Current File?"
        ):
            self.save_file()
        self.path = str()
        self.ui.reset_text()

    def update(self):
        self.ui.update()


program = Main()
while True:
    try:
        program.update()
    except:
        sys.exit()
