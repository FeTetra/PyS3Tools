import sys
import os
import subprocess

from tkinter import filedialog

SCETOOLDIR = "./bin/scetool.exe"

class decryptEboot:
    
    workingDir = "./"
    pwshFix = ""
    
    # Get EBOOT.bin from tkinter file dialog
    input_file_eboot = str(" \'" + filedialog.askopenfilename(initialdir = workingDir, title = "Select EBOOT.BIN", filetypes = (("BIN Files", "*.bin"), ("All Files", "*.*"))) + "\'")
    
    if (os.name == "nt"):
        pwshFix = "powershell "

    print(input_file_eboot)
    
    arg1 = str(pwshFix + SCETOOLDIR + " -i" + input_file_eboot)
    print(arg1)
    
    os.system(arg1)
    