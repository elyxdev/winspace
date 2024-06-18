import os, shutil, glob
def limpiar():
    try:
        if os.path.exists("build/"):
            os.removedirs("build/")
        if os.path.exists("dist/"):
            os.removedirs("dist/")
        if os.path.exists("winspace.spec"):
            os.remove("winspace.spec")
    except:
        pass

def compilar():
    try:
        os.system("pyinstaller --name WinSpace --onefile --uac-admin --clean --icon=./img/new.ico main.py")
    except:
        print("Error al compilar")

if __name__ == "__main__":
    limpiar()
    compilar()
