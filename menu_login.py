USUARIOS = {}


# --- Validaciones usuario - contraseña ---
def validar_usuario(nombre):
    if not nombre:
        print("El nombre de usuario no puede estar vacío.")
        return False
    if nombre in USUARIOS:
        print("El usuario ya existe, elige otro nombre.")
        return False
    return True


def validar_contraseña(contraseña):
    if not contraseña:
        print("La contraseña no puede estar vacía.")
        return False
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    return True


# --- Función para registrar ---
def registrar_usuario():
    nombre = input("Ingrese un nombre de usuario: ").strip()
    if not validar_usuario(nombre):
        return

    contraseña = input("Ingrese una contraseña: ").strip()
    if not validar_contraseña(contraseña):
        return

    USUARIOS[nombre] = contraseña
    print(f"✅ Usuario '{nombre}' registrado con éxito.")


# --- Función para mostrar ---
def mostrar_usuarios():
    if not USUARIOS:
        print("No hay usuarios registrados.")
        return

    print("\n--- Lista de usuarios registrados ---")
    for usuario in USUARIOS:
        print(f"- {usuario}")
    print(f"Total de usuarios: {len(USUARIOS)}")


# --- Función para login ---
def login():
    nombre = input("Ingrese su nombre de usuario: ").strip()
    if nombre not in USUARIOS:
        print("Usuario no encontrado.")
        return

    contraseña = input("Ingrese su contraseña: ").strip()
    if USUARIOS[nombre] != contraseña:
        print("Contraseña incorrecta.")
        return

    print(f"Bienvenido {nombre}, login exitoso.")


# --- Función para el menú de opciones ---
def menu_login():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login()
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


menu_login()
