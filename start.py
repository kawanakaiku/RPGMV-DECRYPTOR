import os # Imports the "os" library
import mvDecryptor # Imports "mvDecryptor.py"

if os.path.exists(os.getcwd()+"/www/data/System.json"): # If they click OK, check if System.json exists.
    mvDecryptor.decryptEntireGame(dir) # If so, decrypt the game.
    print("success")
else: # If it is not found
    pass
    print(os.getcwd()+"/www/data/System.json not found.")
os._exit(0) # Exit the application (avoids memory leaks)