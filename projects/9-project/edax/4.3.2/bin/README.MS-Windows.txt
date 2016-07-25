                      Note for Microsoft Windows users.
                     -----------------------------------

Edax on 32-bit Windows and 64-bit Windows.
-----------------------
In order to run Edax on a win32 (from Windows XP to Windows 7) environment,
launch wEdax-x86.exe. In order to run Edax on a win64 (Vista 64 or Windows 7 64
bits), use wEdax-x64.exe executable. 

Edax runs at about half speed on 32-bits environments, because the program makes
an heavy usage of 64-bits variables. So use the 32-bits version only if you do
not have any other choice.


Using Edax with NBoard
-----------------------
Edax can be run from NBoard, a graphical interface designed by Chris Welty.
You first need to download NBoard from :
http://othellogateway.com/ntest/Ntest/NBoardSetup.msi
Install it: run NBoardSetup.msi and follow the displayed
instructions. 
Then copy the file NBoard.exe into the directory where wEdax is installed.
Rename wEdax into ntest.exe
Now if you click on the NBoard.exe file, it will use Edax as its engine.

Using Edax with Winboard (alien version)
-----------------------------------------
Edax 4.2 can be run from a branch version of winboard supporting reversi as a chess variant. You can download it here:
http://hgm.nubati.net/WinBoard-Alien.zip
Unzip the file in a directory of your choice.
Then launch winboard, for example like this 

winboard /fcp wEdax-x64.exe /fd [directory where you install wEdax-x64.exe] /variant="reversi"

