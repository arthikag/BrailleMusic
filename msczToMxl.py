import subprocess, sys

def convertFile(currentpath):
    p = subprocess.Popen(["powershell.exe", "C:\\Users\\ELCOT\\Desktop\\Braille-Music\\convert.ps1"], stdout=sys.stdout)
    p.communicate()

    # C:\\Users\\ELCOT\\Desktop\\Braille-Music\\convert.ps1