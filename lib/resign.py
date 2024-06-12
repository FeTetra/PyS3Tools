# resign.py

import sys
import os
import subprocess

from tkinter import filedialog

BINDIR = "./bin/"

class decryptEboot:
    
    global input_file_eboot
    global workingDir
    global pwshFix
    
    # Set app working directory and use "powershell" command to run application in Powershell (if Windows is detected)
    workingDir = "./"
    if (os.name == "nt"):
        pwshFix = "powershell "
        
    # Get EBOOT.bin from tkinter file dialog
    input_file_eboot = str(" \'" + filedialog.askopenfilename(initialdir = workingDir, title = "Select EBOOT.BIN", filetypes = (("BIN Files", "*.bin"), ("All Files", "*.*"))) + "\'")
    
    # Get details on the EBOOT
    def getEbootAttributes():
        global isDebugEboot
    
        args = " -i" + input_file_eboot
        os.system(pwshFix + BINDIR + "scetool" + args + "> EBOOTATTR.txt")
        
        with open("EBOOTATTR.txt", 'r') as ebootAttrs:
            checkAttr = ebootAttrs.read()
            
            if ("[DEBUG]") in checkAttr: isDebugEboot = True 
            else: isDebugEboot = False
            
        print(isDebugEboot)
        
    # Function for decrypting retail EBOOT
    def decryptEbootRetail():
        global cmd
        
        if isDebugEboot == True:
            print("This appears to be a debug EBOOT. Choose the \"Decrypt Debug EBOOT\" option to decrypt this binary.")
            exit()
        
        args = " -v -d " + input_file_eboot + " " + workingDir + "EBOOT.ELF"
        cmd = str(pwshFix + BINDIR + "scetool" + args)
        
    # Function for decrypting debug EBOOT
    def decryptEbootDebug():
        global cmd
        
        if isDebugEboot == False:
            print("This appears to be a retail EBOOT. Choose the \"Decrypt Retail EBOOT\" option to decrypt this binary.")
            exit()
        
        args = "" + input_file_eboot + " " + workingDir + "EBOOT.ELF"
        cmd = str(pwshFix + BINDIR + "unfself" + args)
    
    if not input_file_eboot == " \'\'":
        getEbootAttributes()
        decryptEbootDebug()
        #decryptEbootRetail()
        os.system(cmd)
    else:
        print("It appears no EBOOT file was selected. Please select an EBOOT file in order to decrypt.")