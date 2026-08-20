import os


def main():
    """Main

    Se ejecuta cuando es el script pricipal
    """
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub!")


if __name__ == "__main__":
    main()
