import tkinter as tk
from tkinter import filedialog, messagebox

def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("Save It")

def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            self.text_area.delete(1.0, tk.END)
            with open(self.file_path, "r") as file:
                self.text_area.insert(1.0, file.read())
            self.root.title(f"Save It        Current file:{self.file_path}")

def save_file(self):
        if self.file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.file_path, "w") as file:
                    file.write(content)
                messagebox.showinfo("Save File", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Save File", f"Failed to save file: {str(e)}")
        else:
            self.save_as_file()

def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.file_path, "w") as file:
                    file.write(content)
                self.root.title(f"Save It       Current file:{self.file_path}")
                messagebox.showinfo("Save File", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Save File", f"Failed to save file: {str(e)}")

def exit_editor(self):
    self.root.quit()

def show_about(self):
    messagebox.showinfo("About", "This Text Editor is made by Ajmal as mini project in python.This Software GUI is made up using Tkinter.This is only a simple Text Editor which doesnot have much features",)

def set_dark_mode(self):
    self.menu_bar.config(bg='#3E3D3C', fg='white', activebackground='#444444', activeforeground='white')
    self.file_menu.config(bg='#3E3D3C', fg='white')
    self.edit_menu.config(bg='#3E3D3C', fg='white')
    self.help_menu.config(bg='#3E3D3C', fg='white')
    self.mode_menu.config(bg='#3E3D3C', fg='white')
    self.settings_menu.config(bg='#3E3D3C', fg='white')
    self.font_menu.config(bg='#3E3D3C', fg='white')
    self.font_size_menu.config(bg='#3E3D3C', fg='white')
    self.text_area.config(bg="#3E3D3C", fg="white", insertbackground="white")

def set_light_mode(self):
        self.menu_bar.config(bg='#f0f0f0', fg='black', activebackground='#dddddd', activeforeground='black')
        self.file_menu.config(bg='#f0f0f0', fg='black')
        self.edit_menu.config(bg='#f0f0f0', fg='black')
        self.help_menu.config(bg='#f0f0f0', fg='black')
        self.mode_menu.config(bg='#f0f0f0', fg='black')
        self.settings_menu.config(bg='#f0f0f0', fg='black')
        self.font_menu.config(bg='#f0f0f0', fg='black')
        self.font_size_menu.config(bg='#f0f0f0', fg='black')
        self.text_area.config(bg="white", fg="black", insertbackground="black")

def set_special_mode(self):
        self.menu_bar.config(bg='black', fg='green', activebackground='dark green', activeforeground='green')
        self.file_menu.config(bg='black', fg='green')
        self.edit_menu.config(bg='black', fg='green')
        self.help_menu.config(bg='black', fg='green')
        self.mode_menu.config(bg='black', fg='green')
        self.settings_menu.config(bg='black', fg='green')
        self.font_menu.config(bg='black', fg='green')
        self.font_size_menu.config(bg='black', fg='green')
        self.text_area.config(bg="black", fg="green", insertbackground="green")

        self.set_full_screen_mode()

def set_full_screen_mode(self):
        self.full_screen = True
        self.root.attributes("-fullscreen", True)
        self.root.config(menu="")
        self.root.unbind("<Escape>")
        self.root.bind("<Escape>", self.exit_full_screen)

def exit_full_screen(self, event=None):
        self.full_screen = False
        self.root.attributes("-fullscreen", False)
        self.root.config(menu=self.menu_bar)
        self.root.unbind("<Escape>")        

def change_font(self, font_name):
        self.current_font_fam=font_name
        self.text_area.config(font=(self.current_font_fam,self.current_font_size))

def change_font_size(self, size):
        self.current_font_size = size
        self.text_area.config(font=(self.current_font_fam, self.current_font_size))
