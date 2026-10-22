"""Aplicación de consola para administrar un catálogo de productos."""

import sqlite3
import statistics

from base_datos import crear_tabla, registrar_producto, consultar_productos


def pedir_precio():
    """Solicita un precio numérico no negativo."""
    while True:
        entrada = input("Precio del producto: ").strip().replace(",", ".")
        try:
            precio = float(entrada)
        except ValueError:
            print("Dato incorrecto: escribe un precio numérico, por ejemplo 125.50.")
            continue

        if precio < 0:
            print("Dato incorrecto: el precio no puede ser negativo.")
            continue
        return precio


def alta_producto():
    """Solicita datos y registra un producto."""
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("Dato incorrecto: el nombre no puede estar vacío.")
        return

    precio = pedir_precio()
    try:
        registrar_producto(nombre, precio)
    except ValueError as error:
        print(f"Dato incorrecto: {error}")
    else:
        print("Producto registrado correctamente.")


def mostrar_productos():
    """Consulta e imprime los productos guardados."""
    productos = consultar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    print("\n=== Catálogo de productos ===")
    print(f"{'ID':<5}{'Nombre':<25}{'Precio':>12}")
    print("-" * 42)
    for producto_id, nombre, precio in productos:
        print(f"{producto_id:<5}{nombre:<25}${precio:>11.2f}")
    print(f"\nTotal de productos: {len(productos)}")


def mostrar_promedio():
    """Calcula el promedio de los precios registrados."""
    productos = consultar_productos()
    if not productos:
        print("No se puede calcular el promedio: no hay productos registrados.")
        return

    precios = [producto[2] for producto in productos]
    promedio = statistics.mean(precios)
    print(f"Precio promedio de {len(precios)} productos: ${promedio:.2f}")


def main():
    crear_tabla()
    while True:
        print("\n=== Catálogo de productos ===")
        print("1. Registrar producto")
        print("2. Consultar productos")
        print("3. Calcular precio promedio")
        print("4. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            alta_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            mostrar_promedio()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Selecciona una opción del 1 al 4.")


if __name__ == "__main__":
    try:
        main()
    except (sqlite3.Error, OSError) as error:
        print(f"Ocurrió un problema con la base de datos: {error}")
