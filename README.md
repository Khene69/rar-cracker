# Ataque_simple.py – Fuerza Bruta para Archivos RAR

Este script en Python permite realizar un ataque de fuerza bruta con diccionario para descifrar archivos `.rar` protegidos con contraseña, utilizando la herramienta `unrar`.

Este proyecto es solo para fines educativos y de pruebas en archivos propios. No se promueve el uso ilegal o malicioso.

## Cómo funciona

El script recorre línea por línea un diccionario de contraseñas (`.txt`) e intenta abrir el archivo RAR con cada una, usando `unrar`. Si la contraseña es correcta, lo indica y detiene la ejecución.

## Requisitos

- Python 3.x
- `unrar` instalado (y agregado al PATH)
- Archivo `.rar` protegido
- Diccionario `.txt` con posibles contraseñas

## Uso

1. Abre una terminal en la carpeta del script.
2. Ejecuta:

```bash
python Ataque_simple.py
