import Tkinter # Imports the "Tkinter" library
import tkFileDialog # Imports the "tkFileDialog" library
import tkMessageBox # Imports the "tkMessageBox" library
import os # Imports the "os" library
import mvDecryptor # Imports "mvDecryptor.py"

window = Tkinter.Tk() # Create tkinter object
window.wm_withdraw() # Hide blank "tk" window

tkMessageBox.showinfo(title="INFORMATION",message="Please select the game directory.\n(The one that contains the main executable)") # Display a message on screen explaining what directory they need to choose.
dir = tkFileDialog.askdirectory(title="Select Game DIR") # Show a directory selection screen

if dir == (): # If they click cancel
    os._exit(0) # Exit the program

if os.path.exists(dir+"/www/data/System.json"): # If they click OK, check if System.json exists.
    mvDecryptor.decryptEntireGame(dir) # If so, decrypt the game.
    tkMessageBox.showinfo(title="INFORMATION",message="DONE!\nGame has been decrypted.\nAnd an editable file has been created.") # Now show a message saying its done.
else: # If it is not found
    tkMessageBox.showerror(title="ERROR",message="Could not find System.json.\nDid you select the correct directory?") #Display an error message
window.destroy() # Destroy tkinter object
os._exit(0) # Exit the application (avoids memory leaks)
