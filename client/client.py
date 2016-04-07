#!/usr/bin/env python3.4

from gui import Gui
import Tkinter as tk
import requests

class Widok:
    def __init__(self, root):
        self.root = root
        self._gui = Gui(self, root)
        self._gui.pack(side='top', fill='both', expand=True)

    def wez_makiete(self, makieta):
        self._gui.update(makieta)

    def _obsluz_zamkniecie_gui(self):
        get_response = requests.get(url='http://localhost:5000/request_koniec')
        self.root.destroy()

    def obsluz_zdarzenie_oblicz(self):
        dane = {"username":"joeb", "password":"foobar"}
        get_response = requests.post(url='http://localhost:5000/request_oblicz', json=dane)
        self._gui.update(get_response)

if __name__ == '__main__':
    root = tk.Tk()
    widok = Widok(root)
    root.mainloop()

