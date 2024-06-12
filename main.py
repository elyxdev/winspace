import os, json, time, sys, ctypes
from pystyle import Colors, Write
defcol = Colors.blue_to_purple
wp = os.getcwd()
lg_folder = os.path.join(wp, 'lg')
gh_exec = os.path.join(wp, 'gh.exe')
os.chdir(wp)
lg_in = False

def run_as_admin():
    """Ejecuta el script con permisos de administrador."""
    try:
        if sys.argv[-1] != '-admin':
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:
            main()
    except Exception as e:
        jilog(f"No se pudo ejecutar con permisos de administrador: {e}")
        sys.exit(1)

def check_files():
    if not os.path.exists(lg_folder):
        os.mkdir(lg_folder)
    if not os.path.exists(gh_exec):
        jilog("No se encontró el ejecutable de GitHub CLI.")
        time.sleep(4)
        sys.exit(1)

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def jilog(text):
    Write.Print(f"[+] {text}", defcol, 0.01)
    print()

def main():
    global lg_in
    cls()
    # Verifica si está logeado
    os.system("gh auth status > lg/lg_status.lg")
    with open(os.path.join(lg_folder, "lg_status.lg")) as status:
        lineas = status.readlines()
        for linea in lineas:
            if "Logged in to github.com account" in linea:
                if input("Ya has iniciado sesión. Deseas usar esta cuenta? [S/N] > ").lower() == "n":
                    os.system("gh auth logout")
                    return main()
                lg_in = True
                break
        if not lg_in:
            # Loggear
            jilog("Iniciando sesión en GitHub.")
            jilog(f"Copia este código, apreta Enter y pégalo en tu navegador.")
            os.system("gh auth login -p ssh -w --insecure-storage --skip-ssh-key")
    cls()
    # Permisos de codespaces
    jilog("Obteniendo lista de codespaces.")
    os.system("gh codespace list --json name > lg/csnames.lg")
    with open(os.path.join(lg_folder, "csnames.lg"), 'r') as nombres:
        if len(nombres.read()) <= 3:
            jilog("Refrescando permisos de codespaces.")
            jilog(f"Copia este código, apreta Enter y pégalo en tu navegador.")
            os.system("gh auth refresh -h github.com -s codespace")
            os.system("gh codespace list --json name > lg/csnames.lg")
    
    varjson = ""
    with open(os.path.join(lg_folder, "csnames.lg"), 'r') as nombres:
        varjson = json.loads(nombres.read())

    cs_name = ""
    cls()
    if len(varjson) > 1:
        cs_names = []
        for reg in varjson:
            cs_names.append(f"{reg['name']}")
        counter = 0
        jilog("Escoge tu codespace")
        for name in cs_names:
            jilog(f"[{counter}] {name}")
            counter += 1
        cs_name = cs_names[int(input("> "))]
    else:
        cs_name = varjson[0]['name']
    cls()
    os.system(f"title WinSpace: {cs_name} [Elyx] [1.0]")
    os.system(f"gh codespace ssh -c {cs_name}")

    if input("[S/N] Apagar el codespace? > ").lower() == "s":
        os.system(f"gh codespace stop -c {cs_name}")
    jilog("¡Gracias por usar WinSpace!")
    time.sleep(3)
    sys.exit(0)

if __name__ == "__main__":
    cls()
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        jilog("Este script requiere permisos de administrador.")
        run_as_admin()
    os.system("title WinSpace [Elyx] [1.0]")
    check_files()
    main()