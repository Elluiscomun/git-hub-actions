import os

def main():
    nombre = os.getenv('USERNAME', 'usuario')
    print(f"Hola {nombre} desde GitHub")
    print(f"animal")

if __name__ == "__main__":
    main()
