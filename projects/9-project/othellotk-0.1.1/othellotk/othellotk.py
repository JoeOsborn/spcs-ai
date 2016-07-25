#
#   othelloTk  August 2015
#
#   Copyright (C) 2015 John Cheetham    
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
import tkinter.filedialog
import othellotk.dialogs as dlg
import subprocess
import _thread
import time
import os
import shlex
import json
import tkinter.messagebox
import copy
import sys

VERSION = "0.1.1"
BLACK=0
WHITE=1
UNOCCUPIED=-1
COLOUR=("black", "white")
HUMAN=0
COMPUTER=1

class Othello(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # default values for settings
        settings_defaults = {
                         "enginepath": "",
                         "time_per_move": 4,
                         "show_legal_moves": 1
                        }

        self.othellopath = os.path.join(os.path.expanduser("~"), ".othelloTk")
        # create ~/.othelloTk folder if it doesn't exist
        if not os.path.exists(self.othellopath):
            try:
                os.makedirs(self.othellopath)
            except OSError as exc:                
                print("Error - unable to create ~/.othelloTk folder")
                sys.exit(1)

        self.settings_filepath = os.path.join (self.othellopath, "settings.json")
        settings_ok = False
        # read settings from file
        if os.path.exists(self.settings_filepath):
            self.dprint("attempting to read settings from file",self.settings_filepath)
            with open(self.settings_filepath) as settings_file:
                settings_json = json.load(settings_file)
            # check all keys present
            settings_ok = True
            for key in settings_defaults:
                if key not in list(settings_json.keys()):
                    self.dprint("key", key, "is missing")
                    settings_ok = False
        if settings_ok:
            self.dprint("Using settings from",self.settings_filepath)
            self.settings = settings_json
        else:
            self.dprint("Using default settings (unable to get settings from file)")
            self.settings = settings_defaults

        # make resizeable
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W) 
        master.minsize(width=487, height=275)
        self.master = master
        self.master.title('OthelloTk')
        row = []
        for i in range(0, 8):
            row.append(UNOCCUPIED)

        self.board = []
        for i in range(0,8):
            self.board.append(row[:])    

        self.board_hist = [] 
        for i in range(0, 64):
            self.board_hist.append(copy.deepcopy(self.board))

        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board_hist[0] = copy.deepcopy(self.board)

        self.player = [HUMAN, COMPUTER]
        self.stm = BLACK # side to move
        self.first = True
        self.movelist = []
        self.redolist = []
        self.std_start_fen = "8/8/8/3pP3/3Pp3/8/8/8 b - - 0 1"
        self.createWidgets()
        self.gameover = False
        self.engine_active = False
        self.movecount = 0
        self.piece_ids = []
        self.legal_moves = []
        self.engine_init()    # may fail if first run and path not set
        self.after_idle(self.print_board)

    def dprint(self, *args):
        if not debug:
            return
        for i in args: 
            print(i, end=' ')
        print()

    def createWidgets(self):
        # make resizeable
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=2)

        self.line_width = 2
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        board_width = min(screen_width, screen_height) * 0.6
        board_height = board_width

        gap = int(board_width / 25)
        info_bwidth = 10
        pad_frame_border = 5
        pad_frame_width = board_width + int(board_width / 2) + gap + info_bwidth + pad_frame_border*2
        pad_frame = tk.Frame(self, borderwidth=pad_frame_border, width=pad_frame_width, height=board_height, bg="light blue", relief=tk.RIDGE)
        pad_frame.grid(row=0, column=0, sticky="nsew")

        self.canvas = tk.Canvas(pad_frame, borderwidth=0,width=board_width, height=board_height, bg="darkgreen")

        # information frame
        info_frame_width = int(board_width / 2)
        info_frame = tk.Frame(pad_frame, borderwidth=info_bwidth, padx=20,background="DarkSlateBlue", width=info_frame_width, height=board_height, relief=tk.RIDGE)
        set_aspect(self.canvas, info_frame, pad_frame, aspect_ratio=1.0, gap=gap, bordersize=pad_frame_border)
        self.info_frame = info_frame

        # scores
        self.lbl_score_black = tk.StringVar()
        self.lbl_score_white = tk.StringVar()
        self.lbl_score_black.set("* Black 2")
        self.lbl_score_white.set("  White 2")

        self.lbl_black = tk.Label(info_frame, textvariable=self.lbl_score_black, bg="DarkSlateBlue", fg="DarkKhaki")
        self.lbl_white = tk.Label(info_frame, textvariable=self.lbl_score_white, bg="DarkSlateBlue", fg="DarkKhaki")
        self.lbl_black.grid(row=0, column=0, sticky="n")
        self.lbl_white.grid(row=1, column=0, sticky="n")

        # end of game message
        self.eog_text = tk.StringVar()
        self.eog_text.set(" ")
        self.lbl_eog = tk.Label(info_frame, textvariable=self.eog_text, bg="DarkSlateBlue", fg="light blue")
        self.lbl_eog.grid(row=2, column=0, sticky="n")

        def info_resize(event):
            self.info_draw()

        def undo_all():
            self.dprint("undo all")
            if self.movecount == 0:
                self.dprint("can't undo all - already at start position")
                return
            self.gameover = False
            self.command("setboard " + self.std_start_fen + "\n")
            while self.movelist != []:
                mv = self.movelist.pop()
                self.redolist.append(mv)
            self.stm = BLACK
            self.movecount = 0
            self.board = copy.deepcopy(self.board_hist[0])
            self.print_board()
            self.listbox.delete(0, tk.END) # delete all
            self.draw_board()
            self.dprint("self.redolist=",self.redolist)

        def undo():
            self.dprint("undo")
            if self.movecount == 0:
                self.dprint("can't undo - already at start position")
                return
            self.gameover = False

            def undo_move():
                mv = self.movelist.pop()
                self.redolist.append(mv)
                self.movecount -= 1
                self.board = copy.deepcopy(self.board_hist[self.movecount])
                self.stm = abs(self.stm - 1)
                self.print_board()

            # Undo 2 moves so it's still humans move
            self.command("remove\n")  # undo 2 moves in engine
            undo_move()
            if self.stm != BLACK:
                undo_move()

            self.listbox.delete(tk.END)
            self.draw_board()
            self.dprint("self.redolist=",self.redolist)

        def redo():
            self.dprint("redo")
            self.dprint("self.redolist=",self.redolist)
            if self.redolist == []:
                self.dprint("no moves to redo")
                return

            self.command("force\n")

            def redo_move():
                if self.gameover:
                    return
                if self.redolist == []:
                    return
                mv = self.redolist.pop()
                self.command("usermove " + mv + "\n")
                #self.add_move_to_list(mv)
                self.movelist.append(mv)
                self.movecount += 1
                self.board = copy.deepcopy(self.board_hist[self.movecount])
                self.add_move_to_listbox(self.movecount, mv)
                self.stm = abs(self.stm - 1)
                self.print_board()            
                self.gameover = self.check_for_gameover()

            # Redo 2 moves so it's still humans move
            redo_move()
            if self.redolist != []:
                redo_move()

            self.first = True
            self.draw_board()

        def redo_all():
            self.dprint("redo all")
            self.dprint("self.redolist=",self.redolist)
            if self.redolist == []:
                self.dprint("can't redo all - no moves to redo")
                return

            self.command("force\n")
            while self.redolist != []:
                mv = self.redolist.pop()
                self.command("usermove " + mv + "\n")
                #self.add_move_to_list(mv)
                self.movelist.append(mv)
                self.movecount += 1
                self.add_move_to_listbox(self.movecount, mv)
                self.stm = abs(self.stm - 1)

            self.board = copy.deepcopy(self.board_hist[self.movecount])
            self.print_board()
            self.gameover = self.check_for_gameover()
            self.first = True
            self.draw_board()

        scrollbar = tk.Scrollbar(info_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(info_frame, yscrollcommand=scrollbar.set)
        scrollbar.grid(row=3, column=1, sticky="wns")
        self.listbox.grid(row=3, column=0, sticky="ewns")
        scrollbar.config(command=self.listbox.yview)

        self.bbox = tk.Frame(info_frame, bg="black", bd=3, relief=tk.RIDGE)
        self.bbox.grid(row=4, column=0)

        # undo all
        # U+25C0 (9664) left pointing triangle
        self.b1 = tk.Button(self.bbox, text=chr(9664)+chr(9664), command=undo_all)
        self.b1.grid(row=0, column=0)

        # undo
        # U+25C0 (9664) left pointing triangle
        self.b2= tk.Button(self.bbox, text=chr(9664), command=undo) 
        self.b2.grid(row=0, column=1)

        # redo
        # U+25B6 (9654) right pointing triangle
        self.b3 = tk.Button(self.bbox, text=chr(9654), command=redo)
        self.b3.grid(row=0, column=2)

        # redo all
        # U+25B6 (9654) right pointing triangle
        self.b4 = tk.Button(self.bbox, text=chr(9654)+chr(9654), command=redo_all)
        self.b4.grid(row=0, column=3)

        self.bbox.rowconfigure(0, weight=1)
        self.bbox.columnconfigure(0, weight=1)
        self.bbox.columnconfigure(1, weight=1)
        self.bbox.columnconfigure(2, weight=1)
        self.bbox.columnconfigure(3, weight=1)
        info_frame.rowconfigure(0, weight=0)
        info_frame.rowconfigure(1, weight=0)
        info_frame.rowconfigure(2, weight=0)
        info_frame.rowconfigure(3, weight=1)
        info_frame.rowconfigure(4, weight=1)

        info_frame.columnconfigure(0, weight=10)
        info_frame.columnconfigure(1, weight=0)

        info_frame.bind("<Configure>", info_resize)
        self.canvas.bind("<Configure>", self.on_resize)
        self.canvas.bind("<Button-1>", self.clicked)
        self.canvas.bind("<Button-3>", self.rclicked)

        # menubar
        self.master.option_add('*tearOff', tk.FALSE)
        menubar = tk.Menu(self.master)

        menu_file = tk.Menu(menubar)
        menu_edit = tk.Menu(menubar)
        menu_engine = tk.Menu(menubar)
        self.menu_play = tk.Menu(menubar)
        menu_help = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Edit')
        menubar.add_cascade(menu=menu_engine, label='Engine')
        menubar.add_cascade(menu=self.menu_play, label='Play')
        menubar.add_cascade(menu=menu_help, label='Help')

        def about():
            tkinter.messagebox.showinfo("About OthelloTk", "OthelloTk",
                                        detail=VERSION+"\n\nA GUI to play Othello against Edax.\n\n"
                                         "Copyright (c) 2015 John Cheetham\n"
                                         "http://www.johncheetham.com\n\n" 
                                         "This program comes with ABSOLUTELY NO WARRANTY")

        def load_game():
            self.dprint("load game")
            filename = tkinter.filedialog.askopenfilename(filetypes=[("SGF files", "*.sgf")])
            if not filename:
                return
            f = open(filename)
            line=f.readline()
            movelist = []
            while line:
                if line.startswith(";B[") or line.startswith(";W["):
                    if line[3] == "@":
                        mv = line[3:7]
                    else:
                        mv = line[3:5]
                    movelist.append(mv)
                line=f.readline()
            f.close()
            self.new_game(movelist=movelist)

        def save_game():
            self.dprint("save game")
            options = {}
            options['defaultextension'] = ".sgf"
            options['filetypes'] = [("SGF files", "*.sgf")]
            filename = tkinter.filedialog.asksaveasfilename(**options)
            if not filename:
                return
            f = open(filename, 'w')
            f.write("(;GM[2]FF[4]\n")  # Game type 2, File format 4
            f.write("SZ[8]\n")         # board size
            f.write("AP[OthelloTk:"+VERSION+"]\n") # Application used to create the SGF file
            f.write("AB[e4][d5]\n")          # Add black stones at initial position
            f.write("AW[d4][e5]\n")          # Add white stones at initial position
            f.write("PL[B]\n")               # Black player to move first
            stm = BLACK
            side = ("B", "W")
            # write moves
            for move in self.movelist:
                mv = ";" + side[stm] + "[" + move + "]" + "\n"
                f.write(mv)
                stm = abs(stm - 1)
            f.write(")\n")
            f.close()

        def save_settings():
            # save settings to file
            # write to ~/.othelloTk/settings.json
            with open(self.settings_filepath, 'w') as outfile:
                json.dump(self.settings, outfile, indent=4)

        def preferences():
            d = dlg.PreferencesDialog(self.master, self.settings)
            if d.update: 
                save_settings()             # save settings to file
                self.draw_board()           # update show legal moves on board
            return

        def set_engine_path():
            d = dlg.EnginePathDialog(self.master, self.settings)
            if d.update: 
                save_settings()             # save settings to file

        def time_control():
            d = dlg.TimeControlDialog(self.master, self.settings)
            if d.update:
                save_settings()             # save settings to file
                self.command("st " + str(self.settings["time_per_move"]) + "\n") # time per move in seconds

        def move_now(event=None):
            if self.player[self.stm] != COMPUTER:
                return
            self.command("?\n")

        def go(event=None):
            if self.player[self.stm] != COMPUTER:
                return
            self.command("go\n")

        menu_file.add_command(label='New Game', command=self.new_game, underline=0, accelerator="Ctrl+N")
        menu_file.add_command(label='Load Game', command=load_game)
        menu_file.add_command(label='Save Game', command=save_game)
        menu_file.add_separator()
        menu_file.add_command(label='Quit', command=self.quit_program, underline=0, accelerator="Ctrl+Q")
        menu_edit.add_command(label='Preferences', command=preferences)
        menu_engine.add_command(label='Set Engine Path', command=set_engine_path)
        menu_engine.add_command(label='Time Control', command=time_control)
        self.menu_play.add_command(label='Pass', command=self.pass_on_move, underline=0, accelerator="Ctrl+P", state=tk.DISABLED)
        self.menu_play.add_command(label='Move Now', command=move_now, underline=0, accelerator="Ctrl+M", state=tk.DISABLED)
        menu_help.add_command(label='About', command=about, underline=0)
        self.master.config(menu=menubar)

        # accelerator keys
        self.bind_all("<Control-q>", self.quit_program)
        self.bind_all("<Control-n>", self.new_game)
        self.bind_all("<Control-p>", self.pass_on_move)
        self.bind_all("<Control-m>", move_now)
        self.bind_all("<Control-g>", go)

    def info_draw(self):
        width = self.info_frame.winfo_width()
        fontsize = int((width * 0.1) * -1)

        bstm = "  "
        btext = "Black "
        bscore = str(self.count(BLACK))
        if len(bscore) < 2:
            bscore = " " + bscore

        wstm = "  "
        wtext = "White "
        wscore = str(self.count(WHITE))
        if len(wscore) < 2:
            wscore = " " + wscore

        if self.stm == BLACK:
            bstm = "* "
        else:
            wstm = "* "

        self.lbl_score_black.set(bstm+btext+bscore)
        self.lbl_score_white.set(wstm+wtext+wscore)
        self.lbl_black.config(font=("Courier", fontsize, "bold"), padx=width * 0.05)
        self.lbl_white.config(font=("Courier", fontsize, "bold"), padx=width * 0.05)

        self.eog_text.set(" ")
        if self.gameover:
            self.eog_text.set(self.winner_msg)
            self.lbl_eog.config(font=("Courier", int(fontsize/2), "bold"), padx=width * 0.1, pady=width * 0.1)

        self.b1.config(font=("Courier", int(fontsize * 0.6)), fg="MidnightBlue", bg="LightSkyBlue3", activeforeground="blue", activebackground="gainsboro")
        self.b2.config(font=("Courier", int(fontsize * 0.6)), fg="MidnightBlue", bg="LightSkyBlue3", activeforeground="blue", activebackground="gainsboro")
        self.b3.config(font=("Courier", int(fontsize * 0.6)), fg="MidnightBlue", bg="LightSkyBlue3", activeforeground="blue", activebackground="gainsboro")
        self.b4.config(font=("Courier", int(fontsize * 0.6)), fg="MidnightBlue", bg="LightSkyBlue3", activeforeground="blue", activebackground="gainsboro")

        self.listbox.config(font=("Courier", int(fontsize/2)), fg="black", bg="LightSkyBlue3", height=10, width=20)
        self.info_frame.config(padx=fontsize*-1)

    def quit_program(self, event=None):
        self.quit()

    def new_game(self, event=None, movelist=None):
        # start engine if needed
        if not self.engine_active:
            self.engine_init()
            if not self.engine_active:
                self.dprint("Error starting engine")
                # failed to init so display msgbox
                tkinter.messagebox.showinfo("OthelloTk Error", "Error starting engine",
                                       detail="Please Set Engine Path")
                return

        for y in range(0, 8):
            for x in range(0, 8):
                self.board[x][y] = UNOCCUPIED

        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK

        self.listbox.delete(0, tk.END)
        self.movelist = []
        self.redolist = []
        stm = BLACK
        self.movecount = 0
        self.stm = stm # side to move
        self.gameover = False
        self.piece_ids = []
        self.canvas.delete("piece")
        self.canvas.delete("possible_move")

        self.command("setboard " + self.std_start_fen + "\n")
        self.command("force\n")
        if movelist is not None:
            for mv in movelist:
                self.command("usermove " + mv + "\n")
                #self.add_move(x, y)
                self.movelist.append(mv)
                self.movecount += 1
                if mv != "@@@@":                    
                    x, y = self.conv_to_coord(mv)

                    # place piece and flip opponents pieces
                    for incx, incy in [(-1, 0), (-1, -1), (0, -1), (1, -1), (1,0), (1, 1), (0, 1), (-1, 1)]:
                        self.flip(x, y, incx, incy, self.stm)
                try:
                    self.board_hist[self.movecount] = copy.deepcopy(self.board)
                except IndexError:
                    self.dprint("index error on board_hist - appending instead")
                    self.board_hist.append(copy.deepcopy(self.board))
                self.add_move_to_listbox(self.movecount, mv)
                self.stm = abs(self.stm - 1)
                self.print_board()            
                self.gameover = self.check_for_gameover()

        self.draw_board()
        self.first = True
        self.after_idle(self.print_board)
        self.player = [HUMAN, COMPUTER]

    def on_resize(self,event):
        self.draw_board()

    def get_board_size(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        border_size_w = int(canvas_width / 9)
        border_size_h = int(canvas_height / 9)
        board_width = canvas_width - border_size_w
        board_height = canvas_height - border_size_h
        # Make sure width/height is divisible by 8
        board_width = board_width - (board_width % 8)
        board_height = board_height - (board_height % 8)
        x_offset = int(border_size_w / 2)
        y_offset = int(border_size_h / 2)
        return board_width, board_height, x_offset, y_offset, border_size_w, border_size_h

    def draw_board(self):
        board_width, board_height, x_offset, y_offset, border_size_w, border_size_h = self.get_board_size()

        square_width = int(board_width / 8)
        square_height = int(board_height / 8)
        self.canvas.delete(tk.ALL)
        line_width = self.line_width
        # horizontal board lines
        x = 0
        y = 0
        for i in range(0, 9):
            self.canvas.create_line(x + x_offset, y + y_offset, board_width + x_offset, y + y_offset, fill="black", width=line_width, tags="line")
            y += square_height

        # vertical board lines
        x = 0
        y = 0
        for i in range(0, 9):
            self.canvas.create_line(x + x_offset, y + y_offset, x + x_offset, board_height + y_offset, fill="black", width=line_width, tags="line")
            x += square_width

        self.piece_ids = []
        # draw the 4 pieces at start position
        for y in range(0, 8):
            for x in range(0, 8):
                self.draw_piece(x, y)


        fontsize = int(square_width / 4) * -1
        # draw x co-ordinates
        x = square_width
        let="ABCDEFGH"
        for i in range(0, 8):
            #self.canvas.create_text(x, y_offset / 2, font=("Helvetica", fontsize, "bold italic"), text=let[i], fill="light blue")
            self.canvas.create_text(x, int(y_offset/2), font=("Helvetica", fontsize, "italic"), text=let[i], fill="light blue", tags="coords")
            x += square_width

        # draw y co-ordinates
        y = square_width
        num="12345678"
        for i in range(0, 8):
            self.canvas.create_text(int(x_offset/2), y, font=("Helvetica", fontsize, "italic"), text=num[i], fill="light blue", tags="coords")
            y += square_height

    def draw_piece(self, i, j):
        # remove piece (if any) before redrawing it
        for t in self.piece_ids:
            x,y,piece_id = t
            if (x,y) == (i,j):
                self.canvas.delete(piece_id)
                self.piece_ids.remove((x,y,piece_id))
        board_width, board_height, x_offset, y_offset, border_size_w, border_size_h = self.get_board_size()
        square_width = int(board_width / 8)
        square_height = int(board_height / 8)

        # adjustment because we don't want the disc to fill the whole square
        adj =  square_width * 0.1
        tag = "piece"

        if self.board[i][j] == BLACK:
            fill_colour = COLOUR[BLACK]
        elif self.board[i][j] == WHITE:
            fill_colour = COLOUR[WHITE]
        elif (i, j) in self.legal_moves and self.settings["show_legal_moves"]:
            fill_colour = "light blue"
            adj = square_width * 0.45
            tag = "possible_move"
        else:
            return

        x0 = i * square_width + adj + x_offset
        y0 = j * square_height + adj + y_offset
        x1 = (i + 1) * square_width - adj + x_offset
        y1 = (j + 1) * square_height - adj + y_offset
        piece_id = self.canvas.create_oval(x0, y0, x1, y1, fill=fill_colour, tags=tag)
        if tag != "possible_move":
            oval_tup = (i,j,piece_id)
            self.piece_ids.append(oval_tup)

    def add_move_to_listbox(self, moveno, move):
        #fmt = "% *d. " # eg. 1 -> " 1.  "
        #strmv1 = fmt % (3, move)
        if move == "@@@@":
            move = "--"
        strcnt = str(moveno)
        if len(strcnt) < 2:
            strcnt = " " + strcnt
        strcnt = " " + strcnt + ". "
        # if even numbered move add it to the last line (2 moves per line)
        # otherwise add new line
        if moveno % 2 == 0:
            item = self.listbox.get(tk.END) 
            self.listbox.delete(tk.END)
            item = item + "  " + strcnt + move
            self.listbox.insert(tk.END, item)
        else:
            self.listbox.insert(tk.END, strcnt + move)        
        self.listbox.yview(tk.END) # scroll list box to end

    def add_move_to_list(self, move):
        self.redolist = []
        self.movelist.append(move)
        self.movecount += 1
        self.dprint("adding board:",self.movecount)
        try:
            self.board_hist[self.movecount] = copy.deepcopy(self.board)
        except IndexError:
            self.dprint("index error on board_hist - appending instead")
            self.board_hist.append(copy.deepcopy(self.board))
        self.add_move_to_listbox(self.movecount, move)

    def pass_on_move(self, event=None):
        if self.player[self.stm] != HUMAN or self.gameover:
            return
        if self.legal_moves == []:
            self.dprint("no move available - PASS forced")
            self.add_move_to_list("@@@@")
            self.stm = abs(self.stm - 1)
            self.print_board()
            if self.player[self.stm] == COMPUTER:
                str1 = "usermove @@@@\n"
                self.command(str1)

                self.mv = ""
                self.get_computer_move(0)
            return
        self.dprint("Can't pass - legal moves are available")

    # human passes on move (only allowed if no legal moves)
    def rclicked(self, event):
        self.pass_on_move()

    # process humans move (black)
    def clicked(self, event):

        if self.player[self.stm] != HUMAN or self.gameover:
            return

        board_width, board_height, x_offset, y_offset, border_size_w, border_size_h = self.get_board_size()

        # check the click was on the board
        if ((event.x < x_offset) or (event.x > (board_width + x_offset)) or
           (event.y < y_offset) or (event.y > (board_height + y_offset))):
           return

        # get x, y square co-ordinates (in range 0 - 7)
        x = int((event.x - x_offset) / (board_width / 8))
        y = int((event.y - y_offset) / (board_height / 8))

        # start engine if needed
        if not self.engine_active:
            self.engine_init()
            if not self.engine_active:
                self.dprint("Error starting engine")
                # failed to init so display msgbox
                tkinter.messagebox.showinfo("OthelloTk Error", "Error starting engine",
                                       detail="Please Set Engine Path")
                return

        if self.board[x][y] != UNOCCUPIED:
            return
 
        # No legal moves
        if self.legal_moves == []:
            return

        # not a legal move
        if (x, y) not in self.legal_moves:
            return

        # Move is OK - place piece, flip opponents pieces, toggle self.stm
        self.add_move(x, y)

        # convert move from board co-ordinates to othello format (e.g. 3, 5 goes to 'd6')
        l = "abcdefgh"[x]
        n = y + 1
        move = l + str(n)
        self.print_board()
        self.canvas.update_idletasks()
 
        # engine OK - send move
        if self.player[self.stm] == COMPUTER:
            str1 = "usermove " + move + "\n"
            # send human move to engine
            self.command(str1)
            # if it is the engines first move in the game then we need to send the go command
            if self.first:
                self.command('go\n')
                self.first = False

        self.gameover = self.check_for_gameover()
        if self.gameover:
            return
        if self.player[self.stm] == HUMAN:
            return

        # Computers move
        self.mv = ""
        self.get_computer_move(0)
        return

    def add_move(self, x, y):
        # legal move so place piece and flip opponents pieces
        for incx, incy in [(-1, 0), (-1, -1), (0, -1), (1, -1), (1,0), (1, 1), (0, 1), (-1, 1)]:
            self.flip(x, y, incx, incy, self.stm)

        self.stm = abs(self.stm - 1)
        #self.print_board()
        #self.canvas.update_idletasks()

        # convert move from board co-ordinates to othello format (e.g. 3, 5 goes to 'd6')
        l = "abcdefgh"[x]
        n = y + 1
        move = l + str(n)
        self.dprint("move:", move)
        self.add_move_to_list(move)

    # Game is over when neither side can move
    def check_for_gameover(self):
       if self.get_legal_moves(BLACK) == [] and self.get_legal_moves(WHITE) == []:
           self.gameover = True
           black_count = self.count(BLACK)
           white_count = self.count(WHITE)
           if black_count > white_count:
               self.winner_msg = "Game Over - Black wins"
           elif white_count > black_count:
               self.winner_msg = "Game Over - White Wins"
           else:
               self.winner_msg = "Game Over - Match Drawn"
           self.dprint(self.winner_msg)
           self.info_draw()
           return True
       return False

    def print_board(self):
       #print "self.master.winfo_width()=",self.master.winfo_width()
       #print "self.master.winfo_height()=",self.master.winfo_height()
       #for item in self.pad_frame.root.grid_slaves():
       #    print "item=",item

       #tagged = self.canvas.find_withtag("possible_move")
       #for t in tagged:
       #    self.canvas.delete(t)
       self.canvas.delete("possible_move")
       self.legal_moves = self.get_legal_moves(self.stm)
       for y in range(0, 8):
           for x in range(0, 8):
               if (x,y) in self.legal_moves:
                   self.draw_piece(x, y)
       if debug:
           print()
           print("  A B C D E F G H")        
           for y in range(0, 8):
               print(y+1, end=' ')
               for x in range(0, 8):                
                   if self.board[x][y] == BLACK:
                       print("*", end=' ')
                   elif self.board[x][y] == WHITE:
                       print("O", end=' ')                
                   else:
                       if (x, y) in self.legal_moves:
                           print(".", end=' ')
                       else:
                           print("-", end=' ')
               print(y)
           print("  0 1 2 3 4 5 6 7")
           print()
           print("Black:",self.count(BLACK),"   White:",self.count(WHITE))
           if self.stm == BLACK:
               print("black to move")
           else:
               print("white to move")
           print("Legal moves:",self.get_legal_moves(self.stm))
           print()
       self.info_draw()
       if self.player[self.stm] == HUMAN and self.legal_moves == []:
           self.menu_play.entryconfig("Pass",state=tk.NORMAL)
       else:
           self.menu_play.entryconfig("Pass",state=tk.DISABLED)
       #ids = self.canvas.find_all()
       #for id in ids:
       #    tags = self.canvas.gettags(id)[0]
       #    if tags not in ("coords","line"):
       #        print id,self.canvas.gettags(id)
       #print "-"
       #for t in self.piece_ids:
       #    print t, self.canvas.gettags(t[2])


    # count the discs on the board for side
    def count(self, side):
        count = 0
        for y in range(0, 8):
            for x in range(0, 8):
                if self.board[x][y] == side:
                    count += 1
        return count

    def get_legal_moves(self, stm):
        legal_moves = []
        for y in range(0, 8):
            for x in range(0, 8):
                if self.board[x][y] != UNOCCUPIED:
                    continue
                count = 0
                for incx, incy in [(-1, 0), (-1, -1), (0, -1), (1, -1), (1,0), (1, 1), (0, 1), (-1, 1)]:
                    count += self.count_flipped(x, y, incx, incy, stm)
                if count > 0:
                    legal_moves.append((x, y))
        return legal_moves

    def count_flipped(self, x, y, incx, incy, stm):
        count = 0
        opponent = abs(stm - 1)
        xx = x + incx
        yy = y + incy
        while True:
            if xx < 0 or xx > 7 or yy < 0 or yy > 7:
                return 0
            if self.board[xx][yy] == opponent:
                count += 1
            elif self.board[xx][yy] == stm:
                return count
            else:
                return 0
            xx = xx + incx
            yy = yy + incy
        return 0

    # convert move to board coordinates (e.g. "d6" goes to 3, 5)
    def conv_to_coord(self, mv):
        letter = mv[0]
        num = mv[1]
        x = "abcdefgh".index(letter)
        y = int(num) - 1
        return x, y

    # get computers move
    def get_computer_move(self, s=0):
        # Check for move from engine
        for l in self.op:
            l = l.strip()
            if l.startswith('move'):
                self.mv = l[7:]
                break
        self.op = []
        # if no move from engine wait 1 second and try again
        if self.mv == "":
            if s == 0:
                self.dprint("")
                self.dprint("white to move")
                self.b1.config(state=tk.DISABLED)
                self.b2.config(state=tk.DISABLED)
                self.b3.config(state=tk.DISABLED)
                self.b4.config(state=tk.DISABLED)
                self.menu_play.entryconfig("Move Now",state=tk.NORMAL)
            else:
                self.dprint("elapsed ", s, " secs")
            s += 1
            root.after(1000, self.get_computer_move, s)
            return

        self.b1.config(state=tk.NORMAL)
        self.b2.config(state=tk.NORMAL)
        self.b3.config(state=tk.NORMAL)
        self.b4.config(state=tk.NORMAL)
        self.menu_play.entryconfig("Move Now",state=tk.DISABLED)

        self.dprint("move:",self.mv)
        mv = self.mv

        # pass
        if mv == "@@":
            self.stm = abs(self.stm - 1)
            self.add_move_to_list("@@@@")
            self.print_board()
            return

        # convert move to board coordinates (e.g. "d6" goes to 3, 5)
        x, y = self.conv_to_coord(mv)
        #letter = mv[0]
        #num = mv[1]
        #x = "abcdefgh".index(letter)
        #y = int(num) - 1

        for incx, incy in [(-1, 0), (-1, -1), (0, -1), (1, -1), (1,0), (1, 1), (0, 1), (-1, 1)]:
            self.flip(x, y, incx, incy, self.stm)
        self.add_move_to_list(mv)
        self.stm = abs(self.stm - 1)
        self.print_board()
        self.gameover = self.check_for_gameover()

    def engine_init(self):
        self.dprint("Initialising Engine")
        self.engine_active = False
        path = self.settings["enginepath"]
        if not os.path.exists(path):
            self.dprint("Error enginepath does not exist")
            return
        self.dprint("engine path",path)

        arglist = [path,"-xboard", "-n", "1"]
        optionsfile = os.path.join (self.othellopath, "edax.ini")
        if os.path.exists(optionsfile):
            arglist.extend(["option-file", optionsfile])
        self.dprint("subprocess args:",arglist)

        # engine working directory containing the executable
        engine_wdir = os.path.dirname(path)
        self.dprint("engine working directory" ,engine_wdir)

        try:
            p = subprocess.Popen(arglist, stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=engine_wdir)
            self.p = p
        except OSError:
            self.dprint("Error starting engine - check path/permissions")
            #tkMessageBox.showinfo("OthelloTk Error", "Error starting engine",
            #                       detail="Check path/permissions")
            return

        # check process is running
        i = 0
        while (p.poll() is not None):            
            i += 1
            if i > 40:        
                self.dprint("unable to start engine process")
                return False
            time.sleep(0.25)        

        # start thread to read stdout
        self.op = []
        self.soutt = _thread.start_new_thread( self.read_stdout, () )
        #self.command('xboard\n')
        self.command('protover 2\n')

        # Engine should respond to "protover 2" with "feature" command
        response_ok = False
        i = 0
        while True:            
            for l in self.op:
                if l.startswith("feature "):
                    response_ok = True
                    f = shlex.split(l)
                    features = f[1:]
                    for f in features:
                        self.dprint(f)
            self.op = []
            if response_ok:
                break            
            i += 1
            if i > 60:                
                self.dprint("Error - no response from engine")
                return
            time.sleep(0.25)

        self.command('variant reversi\n')
        self.command("setboard " + self.std_start_fen + "\n")
        self.command("st " + str(self.settings["time_per_move"]) + "\n") # time per move in seconds
        #self.command('sd 4\n')
        #sd = "sd " + str(self.settings["searchdepth"]) + "\n"
        #print "setting search depth:",sd
        #self.command(sd)
        self.engine_active = True

    def command(self, cmd):
        try:
            self.p.stdin.write(bytes(cmd, "UTF-8"))
            self.p.stdin.flush()
        except AttributeError:
            self.dprint("AttributeError")
        except IOError:
            self.dprint("ioerror")

    def read_stdout(self):
        while True:
            try:
                self.p.stdout.flush()
                line = self.p.stdout.readline()
                line = line.decode("UTF-8")
                line = line.strip()
                if line == '':
                    self.dprint("eof reached in read_stdout")
                    break  
                self.op.append(line)
            except Exception as e:
                self.dprint("subprocess error in read_stdout:",e)

    def flip(self, x, y, incx, incy, stm):
        count = 0
        opponent = abs(stm - 1)
        xx = x + incx
        yy = y + incy   
        fliplist = [(x, y)]
        while True:
            if xx < 0 or xx > 7 or yy < 0 or yy > 7:
                return 0
            if self.board[xx][yy]== opponent:
                count += 1
                fliplist.append((xx, yy))               
            elif self.board[xx][yy] == stm:
                if count > 0:           
                    for i,j in fliplist:                    
                        self.board[i][j] = stm
                        self.draw_piece(i,j)
                return count                
            else:
                return 0
            xx = xx + incx
            yy = yy + incy

def set_aspect(content_frame, info_frame, pad_frame, aspect_ratio, gap, bordersize):
    # a function which places a frame within a containing frame, and
    # then forces the inner frame to keep a specific aspect ratio

    def enforce_aspect_ratio(event):
        # when the pad window resizes, fit the content into it,
        # either by fixing the width or the height and then
        # adjusting the height or width based on the aspect ratio.

        # start by using the width as the controlling dimension
        desired_width = event.width
        desired_height = int(event.width / aspect_ratio)

        # if the window is too tall to fit, use the height as
        # the controlling dimension
        if desired_height > event.height:
            desired_height = event.height
            desired_width = int(event.height * aspect_ratio)

        # place the window, giving it an explicit size
        desired_width = desired_width * 0.95
        desired_height = desired_height * 0.95

        info_frame_width = int(desired_width / 2)
        tot_width = desired_width + info_frame_width + gap
        #content_frame.place(in_=pad_frame, x=0, y=0, 
        #    width=desired_width, height=desired_height)
        #print "event.width/tot_width=",event.width,tot_width
        x = int((event.width - tot_width) / 2)
        if x < 0:
            x = 0
        content_frame.place(in_=pad_frame, x=x, y=int((event.height - desired_height) / 2) - bordersize, 
            width=desired_width, height=desired_height)
        x = x + desired_width + gap
        info_frame.place(in_=pad_frame, x=x, y=(event.height - desired_height) / 2 - bordersize, 
            width=int(desired_width / 2), height=desired_height)
        #info_frame.place(in_=pad_frame, x=(event.width - tot_width) / 2 + desired_width, y=0, 
        #    width=desired_width / 2, height=desired_height)
        #content_frame.place(in_=pad_frame, x=(event.width - desired_width) / 2, y=(event.height - desired_height) / 2, 
        #    width=desired_width, height=desired_height)
    pad_frame.bind("<Configure>", enforce_aspect_ratio)

def main():
    global root
    global debug
    debug = False
    for arg in sys.argv:
        if arg == "-debug":
            debug = True
    root = tk.Tk()
    app = Othello(root)
    root.aspect(894, 600, 16, 10)
    app.mainloop()

if __name__ == "__main__":
    main()



