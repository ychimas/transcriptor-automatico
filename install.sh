#!/bin/bash

echo "==============================="
echo "Instalando dependencias Python"
echo "==============================="

# Actualizar pip a la última versión
python3 -m pip install --upgrade pip

# Instalar dependencias desde requirements.txt
if [ -f requirements.txt ]; then
    python3 -m pip install -r requirements.txt
else
    echo "Archivo requirements.txt no encontrado."
fi

echo "==============================="
echo "Instalando ffmpeg"
echo "==============================="

# Detectar sistema operativo para instalar ffmpeg
if command -v apt-get &> /dev/null
then
    # Ubuntu/Debian
    sudo apt-get update
    sudo apt-get install -y ffmpeg
elif command -v brew &> /dev/null
then
    # macOS con Homebrew
    brew install ffmpeg
else
    echo "Gestor de paquetes no detectado. Por favor instala ffmpeg manualmente."
fi

echo "==============================="
echo "Instalación completada"
echo "==============================="
