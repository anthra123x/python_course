"""Proyecto 03: Lista de compras.

Una app de consola completa construida con funciones pequeñas.
Cada función hace UNA cosa y bien: así el programa es fácil de leer,
probar y ampliar (mira las ideas de mejora en el README).
"""


def mostrar_menu() -> None:
    """Imprime las opciones disponibles."""
    print("\n" + "=" * 40)
    print("🛒 LISTA DE COMPRAS")
    print("=" * 40)
    print("1. Ver lista")
    print("2. Agregar artículo")
    print("3. Quitar artículo")
    print("4. Vaciar lista")
    print("5. Salir")


def ver_lista(lista: list) -> None:
    """Muestra los artículos numerados."""
    if not lista:
        print("📭 La lista está vacía.")
        return

    print("\nTus compras:")
    # enumerate agrega un índice automáticamente: empezamos en 1.
    for indice, articulo in enumerate(lista, start=1):
        print(f"   {indice}. {articulo}")


def agregar_articulo(lista: list) -> None:
    """Pide un artículo y lo agrega si no está duplicado."""
    articulo = input("¿Qué quieres agregar? ").strip().lower()

    if not articulo:
        print("⚠️ No escribiste nada.")
    elif articulo in lista:
        print(f"ℹ️ '{articulo}' ya está en la lista.")
    else:
        lista.append(articulo)
        print(f"✅ '{articulo}' agregado.")


def quitar_articulo(lista: list) -> None:
    """Quita un artículo si existe."""
    articulo = input("¿Qué quieres quitar? ").strip().lower()

    if articulo in lista:
        lista.remove(articulo)
        print(f"🗑️ '{articulo}' eliminado.")
    else:
        print(f"❌ '{articulo}' no está en la lista.")


def vaciar_lista(lista: list) -> None:
    """Vacía la lista confirmando primero."""
    confirmacion = input("¿Seguro que quieres vaciar TODO? (sí/no): ").strip().lower()

    if confirmacion in ("si", "sí", "s", "yes", "y"):
        lista.clear()          # .clear() deja la lista vacía
        print("🗑️ Lista vaciada.")
    else:
        print("✅ Operación cancelada.")


def main() -> None:
    """Punto de entrada: controla el menú principal."""
    compras = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            ver_lista(compras)
        elif opcion == "2":
            agregar_articulo(compras)
        elif opcion == "3":
            quitar_articulo(compras)
        elif opcion == "4":
            vaciar_lista(compras)
        elif opcion == "5":
            print("👋 ¡Hasta la próxima!")
            break              # única salida del while True
        else:
            print("⚠️ Opción inválida. Escribe un número del 1 al 5.")


if __name__ == "__main__":
    main()