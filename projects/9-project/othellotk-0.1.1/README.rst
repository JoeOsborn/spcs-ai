OthelloTk
---------

Edax gui to play Othello against the Edax engine.
Written in python3/Tkinter and licensed under the GPL v3+
(see the file named LICENSE).
It was tested with edax 4.3.2 and Python 3.4.3 on Linux.

Requirements
------------
Python 3, tkinter, Edax.

Running OthelloTk
-----------------
There are 3 ways to install/run it.

 1. Run it from the source folder by running the run.py script:

        python run.py

 2. Install it on your system with the command:

        python setup.py install

        This command should be run as root user.
        You can then run it with the command 'othellotk'.

 3. Install it from PyPI

        pip install othellotk

        You can then run it with the command 'othellotk'.

Setting up the Engine Path
--------------------------
 1. Download the edax othello engine from http://abulmo.perso.neuf.fr
    This has a prebuilt binary for Linux 64 bit.

 2. Start othelloTk.

 3. Do Engine/Set Engine Path and set the engine path to the edax
    executable.
    This is called lEdax-x64 in the edax bin folder (if you are using
    Linux 64 bit).

 4. Start the game by left clicking to place a black stone.

Usage
-----
You play black, computer plays white.
Click on a square to place a black stone.
If you find there are no legal moves then you can pass by right
clicking anywhere on the board.

Edax allows you to configure engine settings in a file named
edax.ini. Copy this file into the ~/.othelloTk/ folder
(or into the edax bin folder). See edax documentaion for more on this.

To display debug messages use the -debug flag:

    python run.py -debug
    (or othelloTk -debug if installed)

If the engine is taking too long to move you can use ctrl-m to make it
move instantly. Use the time control menu option to set the time to
move.
