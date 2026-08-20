import os


def main():
    """Se ejecuta cuando es el script pricipal
    """
    nombre = os.getenv("USERNAME")
    lenguaje = os.getenv("LANGUAGE")
    print(f"¡Hola, mi nombre es {nombre} y te saludo desde GitHub! y mi lenguaje favorito es {lenguaje}")


if __name__ == "__main__":
    main()
