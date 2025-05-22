# Proyecto de Transcripción de Audio con Whisper
 
*Transcribe audios automáticamente con IA*

Este proyecto permite transcribir audios a texto usando el modelo Whisper de OpenAI, generando archivos HTML con las transcripciones sincronizadas.

---

## 🚀 Características Principales
- ✅ Transcripción automática con marcas de tiempo
- ✅ Soporte para múltiples formatos de audio (MP3, WAV, etc.)
- ✅ Generación de HTML listo para integrar en tu proyecto
- ✅ Fácil configuración en Windows/Linux/macOS

## 📂 Estructura del Proyecto

- `audios/` — Carpeta donde se deben colocar los archivos de audio para transcribir.
- `output/` — Carpeta donde se guardan las transcripciones generadas.
- `install.bat` — Script para instalar dependencias en Windows.
- `install.sh` — Script para instalar dependencias en Linux/macOS.
- `requirements.txt` — Lista de dependencias Python necesarias.
- `transcribe.py` — Script principal para transcribir archivos de audio.

---

## ⚙️ Requisitos

- Python 3.10 o superior
- ffmpeg instalado y accesible en el PATH, Recomendado con Chocolatey
- Conexión a internet para instalar paquetes

---

## (Recomendado con Chocolatey):

   ```bash
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```
---

## 🛠 Instalación

### En Windows

1. Ejecuta el archivo `install.bat` **como administrador**:
   - Haz clic derecho sobre `install.bat`.
   - Selecciona "Ejecutar como administrador".
2. Esto garantiza que las dependencias se instalen correctamente.

### En Linux/macOS

1. Abre una terminal.
2. Da permisos de ejecución al script con:
   ```bash
   chmod +x install.sh
   sudo ./install.sh

---
## 🎯 Uso

1. Coloca tus audios en /audios
2. Ejecuta:
   ```bash
   python transcribe.py
3. Resultados en /output/*.html
