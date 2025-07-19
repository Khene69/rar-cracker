import subprocess

def crack_rar_unrar(rar_path, wordlist_path):
    with open(wordlist_path, "r", encoding="latin-1") as f:
        for line in f:
            pwd = line.strip()
            # Comando para probar contraseña 
            cmd = ['unrar', 't', f'-p{pwd}', rar_path]

            try:
                result = subprocess.run(cmd, capture_output=True, text=True)
                output = result.stdout + result.stderr

                if "All OK" in output:
                    print(f"\n✅ ¡El Mish es clave! --> {pwd}")
                    return
                else:
                    print(f"❌ Mala tu wea: {pwd}")
            except Exception as e:
                print(f"⚠️ Error con '{pwd}': {e}")

    print("\n❌ NI cagando sacai esa contrasseña ql.")

if __name__ == "__main__":
    rar_file = input("Ingresa la ruta del archivo RAR : ").strip()
    wordlist = input("Ingresa la ruta del diccionario ").strip()
    crack_rar_unrar(rar_file, wordlist)

