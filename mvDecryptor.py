# RPG Maker MV Decryption Script
#
# Created By SilicaAndPina 1/12/2018
#
#

import binascii # Imports the "binascii" library
import os # Imports the "OS" library


def xor(data, key): # XOR Encryption / Decryption Algorithm
    l = len(key) # Sets l to length of key.
    return bytearray(((data[i] ^ key[i % l]) for i in range(0,len(data))))  # Do complex MATH stuff and convert the result to a bytearray.

def findKey(gameDir): # Function for finding decryption key
    key = open(gameDir+"/www/data/System.json","rb").read() # Read System.json
    key = key[key.index('"encryptionKey":"')+len('"encryptionKey":"'):] # Find "encryptionKey":" in System.json
    key = key[:key.index('"}')] # Finish string at "}
    return bytearray(binascii.unhexlify(key)) # Decode Hexadecimal and convert to ByteArray.

def decryptFilename(encryptedFilename): # Function for "Decrypting" a filename
    if encryptedFilename.endswith(".rpgmvo"): # If file extension is .rpgmvo
        return encryptedFilename[:-7]+".ogg" # Make .ogg file.
    if encryptedFilename.endswith(".rpgmvm"): # If file extension is .rpgmvm
        return encryptedFilename[:-7] + ".m4a" # Make .m4a file.
    if encryptedFilename.endswith(".rpgmvp"): # If file extension is .rpgmvp
        return encryptedFilename[:-7] + ".png" # Make .png file.

def isEncryptedFile(path): # Function for determining if the specified path is an Encrypted RMMV File..
    if path.endswith(".rpgmvo"): # If file extension is .rpgmvo
        return True # Yes it is an encrypted RMMV File.
    if path.endswith(".rpgmvm"): # If file extension is .rpgmvm
        return True # Yes it is an encrypted RMMV File.
    if path.endswith(".rpgmvp"): # If file extension is .rpgmvp
        return True # Yes it is an encrypted RMMV File.

def decryptFile(encryptedFilename,key): # Function for decrypting a file.
    dfile = decryptFilename(encryptedFilename)
    ctime = os.stat(encryptedFilename).st_ctime
    file = open(encryptedFilename,"rb").read() # Read encrypted file.
    file = file[16:] # Remove file header.
    cyphertext = bytearray(file[:16]) # Read encrypted file header.
    plaintext = str(xor(cyphertext,key)) # Decrypt file header
    file = file[16:] # Remove decrypted file header
    open(dfile,"wb").write(plaintext + file) # Write decrypted file header + rest of file to disk as Decrypted Filename..
    os.utime(dfile, (ctime, ctime))


def decryptEntireGame(gameDir): # Function for decrypting an entire game folder.
    key = findKey(gameDir) # Find Decryption Key
    for path, dirs, files in os.walk(gameDir+"/www"): # List all files inside the Game's project folder.
        for f in files: # For all files in Game's WWW folder.
            if isEncryptedFile(os.path.join(path,f)): # If its an encrypted RM MV File...
                decryptFile(os.path.join(path,f),key) # Decrypt the file.
                os.remove(os.path.join(path,f)) # Delete encrypted file
    SystemJson = open(gameDir+"/www/data/System.json","rb").read() # Reads System.json
    SystemJson = SystemJson.replace('"hasEncryptedImages":true','"hasEncryptedImages":false') # Sets hasEncryptedImages to FALSE
    SystemJson = SystemJson.replace('"hasEncryptedAudio":true','"hasEncryptedAudio":false') # Sets hasEncryptedAudio to FALSE
    open(gameDir+"/www/data/System.json","wb").write(SystemJson) # Writes new System.json to disk
    open(gameDir+"/www/Game.rpgproject","wb").write("RPGMV 1.0.0") # Creates Editable RPG Maker MV Project File

