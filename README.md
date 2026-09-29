# WinSpace 🚀☁️

![WinSpace](img/banner.png) *(Puedes añadir un banner o captura de pantalla en `img/banner.png`)*

**WinSpace** es una herramienta interactiva de consola escrita en Python diseñada para conectar, gestionar y autorizar **GitHub Codespaces** de una manera sencilla, estética y guiada. Actúa como un *wrapper* inteligente alrededor de la CLI oficial de GitHub (`gh`), automatizando el flujo de autenticación y conexión.

## ✨ Características

*   **Interfaz Estética:** Utiliza `pystyle` para mostrar menús y textos coloridos e intuitivos directamente en la terminal.
*   **Gestión Automática de Autenticación:** Detecta si ya tienes una sesión activa de GitHub. Si no, genera el código de autenticación y te guía automáticamente a tu navegador.
*   **Aislamiento de Entorno:** Maneja permisos de ejecución y puede escalar privilegios (ejecución como Administrador) en sistemas Windows de forma automática.
*   **Soporte Multiplataforma:** Diseñado para funcionar en Windows (`.bat`) y sistemas basados en Unix (`.sh`), mapeando correctamente los binarios locales de la CLI de GitHub.

## 🛠️ Tecnologías Usadas

*   **Lenguaje:** Python 3.x
*   **Librerías Destacadas:** `pystyle` (interfaz visual)
*   **Dependencia Externa:** [GitHub CLI (`gh`)](https://cli.github.com/) (debe estar instalada en tu sistema).

## 🚀 Instalación y Uso

1.  **Pre-requisitos:**
    Asegúrate de tener instalados **Python 3** y la **CLI de GitHub (`gh`)**.

2.  **Clona este repositorio:**
    ```bash
    git clone https://github.com/elyxdev/winspace.git
    cd winspace
    ```

3.  **Ejecuta el programa:**
    Puedes iniciar directamente usando los scripts preparados que se encargarán de instalar las dependencias (`pystyle`) si faltan:
    
    *   **En Windows:**
        ```cmd
        iniciar.bat
        ```
    *   **En Linux / macOS:**
        ```bash
        bash iniciar.sh
        ```

    También puedes correr el archivo principal directamente si ya tienes las librerías necesarias:
    ```bash
    python main.py
    ```

## 📂 Compilación

Si deseas distribuir el script como un ejecutable `.exe` cerrado, el proyecto incluye un script de compilación `build.py` y accesos directos:
*   Windows: `compilar.bat`
*   Linux/macOS: `bash compilar.sh`

## 👨‍💻 Autor

Creado y desarrollado por **Elyx** ([@elyxdev](https://github.com/elyxdev)).

¡Si encuentras útil esta herramienta, no dudes en dejar una estrella en el repositorio! Cualquier aporte (Pull Request) o reporte de bug es bienvenido.
