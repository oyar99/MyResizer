#!/usr/bin/python3

"""
main_view.py
"""

import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from .algorithms.image_manip import read_image_as_2D_array, write_2D_array_as_image
from .algorithms.image_energy import compute_energy, energy_data_to_colors
from .algorithms.resizer import compute_vertical_seam, remove_seam_from_image
import threading
from PIL import Image

class MainView(tk.Frame):
    """
    Represents the main frame of the app
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.img = None
        self.parent = parent
        self.pixels_label = tk.Label(self.parent, text='Number of columns to remove')
        self.pixels_slider = tk.Scale(self.parent, from_=1, to=100, orient=tk.HORIZONTAL, length=100//2)
        self.button_resize = tk.Button(self.parent, text='Resize image', command=self.select_folder_to_save)

        button_loadImage = tk.Button(self.parent, text='Upload image', command=self.select_image)
        button_loadImage.pack()

    def select_image(self):
        """
        Prompts the user to open an image file
        """

        filetypes = [
            ('Image files', ('.png', '.jpg')),
        ]

        filename = filedialog.askopenfilename(title='Open a file', initialdir='/',filetypes=filetypes)

        if len(filename) > 0:
            self.img = Image.open(filename)

            w, h = self.img.size

            self.pixels_slider = tk.Scale(self.parent, from_=1, to=w, orient=tk.HORIZONTAL, length=w//2)
            self.pixels_label.pack()
            self.pixels_slider.pack()
            self.button_resize.pack()

    def select_folder_to_save(self):
        """
        Prompts the user to select a folder to save the resized image
        """

        filetypes = [
            ('Image files', '.png')
        ]

        filename = filedialog.asksaveasfilename(title='Save as', filetypes=filetypes)

        thread = threading.Thread(target=lambda:self.resize_image(filename, self.pixels_slider.get()))
        thread.start()


    def resize_image(self, filename, colsToRemove):
        raw_img = read_image_as_2D_array(self.img)

        for i in range(colsToRemove):
            energy_data = compute_energy(raw_img)
            #energy_pixels = energy_data_to_colors(energy_data)
            #energy_image = write_2D_array_as_image(energy_pixels)
            #energy_image.save('energyImage.png')
            seam_path = compute_vertical_seam(energy_data)
            raw_img = remove_seam_from_image(raw_img, seam_path)
            print(f'removed {i}th seam')

        resized_img = write_2D_array_as_image(raw_img)
        resized_img.save('result.png')



