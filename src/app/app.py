#!/usr/bin/python3

"""
app.py
"""

from tkinter import ttk
import tkinter as tk
from constants import window
from core.main_view import MainView

class App(tk.Frame):
    """
    Represents the starting point of the app
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        parent.title(window.TITLE)
        parent.iconbitmap(window.ICON_PATH)
        parent.geometry(window.SCREEN_SIZE)

        # configures a tab controller
        tab_control = ttk.Notebook(parent)
        tab_main = tk.Frame(tab_control)
        tab_about = tk.Frame(tab_control)
        tab_control.add(tab_main, text=window.MAIN_TAB_TITLE)
        tab_control.add(tab_about, text=window.ABOUT_TAB_TITLE)
        tab_control.pack(expand=True, fill=tk.BOTH)

        # configures main tab
        MainView(tab_control).pack()



if __name__ == '__main__':
    root = tk.Tk()
    App(root).pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
    root.mainloop()