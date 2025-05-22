@echo off
SETLOCAL

:: Establece la carpeta actual como base
cd /d %~dp0

echo ===============================
echo Instalando dependencias Python
echo ===============================
pip install -r requirements.txt

echo ===============================
echo Instalando ffmpeg con Chocolatey
echo ===============================

:: Verifica si choco está disponible
where choco >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Chocolatey no está instalado.
    echo 🔧 Por favor instálalo desde: https://chocolatey.org/install
    pause
    exit /b 1
)

choco install ffmpeg -y

echo ===============================
echo ✅ Instalación completada
echo ===============================
pause
