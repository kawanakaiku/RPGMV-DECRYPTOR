from https://bitbucket.org/SilicaAndPina/rpgmv-decryptor/src/master/

runs on python3

# RPGMV-DECRYPTOR            
Decrypts RPG Maker MV Game Files (.rpgmvo, .rpgmvp and .rpgmvm files)         
and creates an .rpgproject editable file.        
Reverse Engineering / Static Analysis & Modding purposes~ plz dont steal assets. .           

Written in Python 2.7.

# How RPGMV Crypto Works
RPG Maker MV's encryption is really weak, for startas it doesnt even encrypt the entire file, it just encrypts the header using XOR. and then writes its own RPG Maker MV header to the file with the old (now encrypted) header under it.
the encryption key is just an md5 hash of whatever was entered into the encryption key box under deployment in the rpg maker engine itself. and can be easily read from www\data\System.json, so all you need to do is
XOR the encrypted header using the md5 hash inside System.json as the key and remove the RPG Maker MV header. 

System.json contains 2 boolean values of
hasEncryptedImages and hasEncryptedMusic
which are used to indicate whther or not the game has encrypted music and or images
this is pretty important because otherwise the game cant tell if it needs to decrypt the assets before loading them in game.
this program will set both these values to "false" after the game has been decrypted. to avoid issues.

The .rpgproject file is just a plaintext file that contains the string "RPGMV %s" where %s is whatever version of RPG Maker MV the Project was last loaded in so i just use version 1.0.0 because its the first version and will basicly mean that the project can be loaded in any version of RPG Maker MV the actural project itself *is* the decrypted www/ directory.
  
Downloads:   
Windows (x86): https://bitbucket.org/SilicaAndPina/rpgmv-decryptor/downloads/RPGMV-DECRYPTOR-WIN32.zip  
Linux: https://bitbucket.org/SilicaAndPina/rpgmv-decryptor/downloads/RPGMV-DECRYPTOR-LINUX.tar.gz  
