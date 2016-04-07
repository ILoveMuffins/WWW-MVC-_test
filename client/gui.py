#!/usr/bin/env python3.4

import Tkinter as tk
from makieta import Makieta

class Gui(tk.Frame):
    def __init__(self, parent, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self._parent = parent
        self._root = root
        self._root.title('Materialy')
        self._zainicjuj_grafike()
        self.center(self._root)
        self._root.protocol('WM_DELETE_WINDOW', self._parent._obsluz_zamkniecie_gui)

    def _zainicjuj_grafike(self):
        self._root.minsize(width=400, height=200)
        self._root.maxsize(width=400, height=450)

        self._button = tk.Button(text="oblicz", command=self._parent.obsluz_zdarzenie_oblicz)
        self._button.pack()

        self._label3 = tk.Label(self._root, text="Wynik:")
        self._label3.pack(anchor='w')

        self._label4 = tk.Label(self._root)
        self._label4.pack(anchor='w')

    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def update(self, response):
        self._label4.config(text=response.text)

