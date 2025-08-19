usuarios = {}


# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Ingrese un nombre de usuario: ").strip()

    if not nombre:
        print("⚠️ El nombre de usuario no puede estar vacío.")
        return

    if nombre in usuarios:
        print("❌ El usuario ya existe, elige otro nombre.")
        return

    contraseña = input("Ingrese una contraseña: ").strip()
    if not contraseña:
        print("⚠️ La contraseña no puede estar vacía.")
        return

    usuarios[nombre] = contraseña
    print(f"✅ Usuario '{nombre}' registrado con éxito.")


# Función para mostrar todos los usuarios
def mostrar_usuarios():
    if not usuarios:
        print("📭 No hay usuarios registrados.")
    else:
        print("\n--- Lista de usuarios registrados ---")
        for usuario in usuarios:
            print(f"- {usuario}")
        print(f"👥 Total de usuarios: {len(usuarios)}")


# Función para loguear
def login():
    nombre = input("Ingrese su nombre de usuario: ").strip()
    if nombre in usuarios:
        contraseña = input("Ingrese su contraseña: ").strip()
        if usuarios[nombre] == contraseña:
            print(f"🔓 Bienvenido {nombre}, login exitoso.")
        else:
            print("❌ Contraseña incorrecta.")
    else:
        print("❌ Usuario no encontrado.")
    print("➡️ Intento de login finalizado.")


# Función principal con menú
def menu():
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
            print("👋 Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Intente de nuevo.")


menu()
