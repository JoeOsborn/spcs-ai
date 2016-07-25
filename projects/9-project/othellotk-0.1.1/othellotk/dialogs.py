#
#   dialogs.py
#
#   This file is part of othelloTk   
#
#   othelloTk is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   othelloTk is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with othelloTk.  If not, see <http://www.gnu.org/licenses/>.
#   

import tkinter as tk
import os
import tkinter.simpledialog
import tkinter.filedialog

class PreferencesDialog(tkinter.simpledialog.Dialog):
    def __init__(self, master, settings):
        self.settings = settings
        self.show_legal_moves = tk.IntVar()
        self.show_legal_moves.set(settings["show_legal_moves"])
        self.update = False
        tkinter.simpledialog.Dialog.__init__(self, master)

    def body(self, master):
        c = tk.Checkbutton(master, text="Show Legal Moves", variable=self.show_legal_moves)
        c.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)
        if self.show_legal_moves.get() == 1:
            c.select()
        return c # initial focus

    def apply(self):
        self.settings["show_legal_moves"] = self.show_legal_moves.get()
        self.update = True
        return

class EnginePathDialog(tkinter.simpledialog.Dialog):
    def __init__(self, master, settings):
        self.settings = settings
        self.enginepath = tk.StringVar()
        self.enginepath.set(settings["enginepath"])
        self.update = False
        tkinter.simpledialog.Dialog.__init__(self, master)

    def body(self, master):
        tk.Label(master, text="Engine Path:").grid(row=2, sticky=tk.W)
        tk.Button(master, text="Browse", command=self.get_engine_path).grid(row=2, column=2)
        self.e1 = tk.Entry(master, textvariable=self.enginepath, width=30)
        self.e1.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        self.msg = tk.StringVar()
        self.msg.set("Please set a valid path to the Edax engine")
        msglbl = tk.Label(master, textvariable=self.msg, justify=tk.LEFT).grid(row=3, column=1, sticky=tk.W)
        return self.e1 # initial focus

    def validate(self):
        enginepath = self.enginepath.get()
        if os.path.exists(enginepath): 
            return True
        else:
            self.msg.set("Not a valid path")
            return False

    def apply(self):
        self.settings["enginepath"] = self.e1.get()
        self.update = True
        return

    def get_engine_path(self):
        filename = tkinter.filedialog.askopenfilename()
        self.enginepath.set(filename)

class TimeControlDialog(tkinter.simpledialog.Dialog):
    def __init__(self, master, settings):
        self.settings = settings
        self.time_per_move = tk.IntVar()
        self.time_per_move.set(settings["time_per_move"])
        self.update = False
        tkinter.simpledialog.Dialog.__init__(self, master)

    def body(self, master):
        tk.Label(master, text="Time per Move (seconds):").grid(row=2, sticky=tk.W)
        self.e1 = tk.Entry(master, textvariable=self.time_per_move, width=4)
        self.e1.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        return self.e1 # initial focus

    def validate(self):
        tpm = self.e1.get()
        try: 
            x = int(tpm)
            if x < 0:
                return False
            return True
        except ValueError:
            return False

    def apply(self):
        self.settings["time_per_move"] = self.e1.get()
        self.update = True
        return

