"""Funciones para crear y consultar la base de datos SQLite del catálogo."""

import sqlite3
from contextlib import closing
from pathlib import Path

RUTA_BD = Path(__file__).resolve().parent / "catalogo.db"


def crear_tabla():
    """Crea la tabla productos si todavía no existe."""
    with closing(sqlite3.connect(RUTA_BD)) as conexion:
        with conexion:
            conexion.execute(
                """
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL CHECK (precio >= 0)
                )
                """
            )


def registrar_producto(nombre, precio):
    """Valida y guarda un producto en la base de datos."""
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre del producto no puede estar vacío.")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    with closing(sqlite3.connect(RUTA_BD)) as conexion:
        with conexion:
            conexion.execute(
                "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
                (nombre.strip(), precio),
            )


def consultar_productos():
    """Devuelve los productos registrados, ordenados por id."""
    with closing(sqlite3.connect(RUTA_BD)) as conexion:
        with conexion:
            cursor = conexion.execute(
                "SELECT id, nombre, precio FROM productos ORDER BY id"
            )
            return cursor.fetchall()
