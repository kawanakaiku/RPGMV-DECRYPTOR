import os # Imports the "os" library
import mvDecryptor # Imports "mvDecryptor.py"

dir = os.getcwd()
system_json = os.path.join(dir, "./www/data/System.json")

if os.path.exists(system_json): # If they click OK, check if System.json exists.
    mvDecryptor.decryptEntireGame(dir) # If so, decrypt the game.
    print("success")
else: # If it is not found
    pass
    print(system_json + " not found.")
os._exit(0) # Exit the application (avoids memory leaks)
