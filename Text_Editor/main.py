import tkinter as tk
from tkinter import scrolledtext
from assets import functions as fun

# Fixing blur DPI awareness (Windows specific)
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('./assets/logo.ico')
        self.root.title("Save It")
        self.root.geometry("800x600")
        self.root.minsize(400, 400)

        self.current_font_fam = "Helvetica"
        self.current_font_size = 14

        self.text_area = scrolledtext.ScrolledText(self.root, undo=True, wrap=tk.WORD, font=(self.current_font_fam, self.current_font_size), bg='#3E3D3C', foreground='white', insertbackground='white')
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

        self.mode_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Mode", menu=self.mode_menu)
        self.mode_menu.add_command(label="Dark Mode", command=self.set_dark_mode)
        self.mode_menu.add_command(label="Light Mode", command=self.set_light_mode)
        self.mode_menu.add_command(label="Special Mode", command=self.set_special_mode)

        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

        self.font_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.settings_menu.add_cascade(label="Font", menu=self.font_menu)

        available_fonts = [
            'Helvetica', 'Arial', 'Times New Roman', 'Courier New', 'Verdana',
            'Tahoma', 'Terminal', 'Comic Sans MS', 'Calibri', 'Impact', 'Georgia', 'Segoe UI', 'Palatino', 'Linotype', 'Freestyle Script', 'Lucida Handwriting'
        ]

        for font_name in available_fonts:
            self.font_menu.add_command(label=font_name, command=lambda f=font_name: self.change_font(f))

        self.font_size_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.settings_menu.add_cascade(label="Font Size", menu=self.font_size_menu)

        available_font_sizes = [8, 10, 12, 14, 16, 18, 20, 22, 24]

        for size in available_font_sizes:
            self.font_size_menu.add_command(label=str(size), command=lambda s=size: self.change_font_size(s))

        self.file_path = None

    def new_file(self):
        fun.new_file(self)

    def open_file(self):
        fun.open_file(self)

    def save_file(self):
        fun.save_file(self)

    def save_as_file(self):
        fun.save_as_file(self)

    def exit_editor(self):
        fun.exit_editor(self)

    def show_about(self):
        fun.show_about(self)

    def set_dark_mode(self):
        fun.set_dark_mode(self)

    def set_light_mode(self):
        fun.set_light_mode(self)

    def set_special_mode(self):
        fun.set_special_mode(self)

    def set_full_screen_mode(self):
        fun.set_full_screen_mode(self)

    def exit_full_screen(self, event=None):
        fun.exit_full_screen(self, event)

    def open_preferences(self):
        fun.open_preferences(self)

    def change_font(self, font_name):
        fun.change_font(self, font_name)

    def change_font_size(self, size):
        fun.change_font_size(self, size)
    

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
