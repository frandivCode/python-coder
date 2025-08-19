usuarios = {}


# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Ingrese un nombre de usuario: ")
    if nombre in usuarios:
        print("❌ El usuario ya existe.")
    else:
        contraseña = input("Ingrese una contraseña: ")
        usuarios[nombre] = contraseña
        print("✅ Usuario registrado con éxito.")


# Función para mostrar todos los usuarios
def mostrar_usuarios():
    if not usuarios:
        print("📭 No hay usuarios registrados.")
    else:
        print("\n--- Lista de usuarios registrados ---")
        for usuario in usuarios:
            print(f"- {usuario}")


# Función para loguear
def login():
    nombre = input("Ingrese su nombre de usuario: ")
    if nombre in usuarios:
        contraseña = input("Ingrese su contraseña: ")
        if usuarios[nombre] == contraseña:
            print(f"🔓 Bienvenido {nombre}, login exitoso.")
        else:
            print("❌ Contraseña incorrecta.")
    else:
        print("❌ Usuario no encontrado.")


# Función principal con menú
def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login()
        elif opcion == "4":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción inválida. Intente de nuevo.")


menu()
