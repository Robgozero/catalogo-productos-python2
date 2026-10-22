# Catálogo de productos con Python y SQLite

**Materia:** Programación Avanzada  
**Unidad:** 6 — Módulos y paquetes  
**Archivo principal:** `main.py`

## Descripción

Aplicación de consola para registrar productos, consultar el catálogo almacenado en SQLite y calcular el precio promedio utilizando `statistics`.

## Estructura del proyecto

- `main.py`: menú, captura de datos, consulta del catálogo y cálculo del promedio.
- `base_datos.py`: creación de la tabla, registro y consulta de productos. Las conexiones se cierran correctamente.
- `catalogo.db`: archivo creado automáticamente en la primera ejecución. No es necesario subirlo a GitHub.
- `evidencias/`: carpeta para guardar las capturas reales de las pruebas.

## Versión de Python

La solución utiliza sintaxis compatible con Python 3.10 o posterior. Para documentar la versión utilizada en tu equipo, ejecuta:

```bash
python --version
```

## Módulos utilizados

- `sqlite3`: permite utilizar la base de datos SQLite.
- `statistics`: calcula la media aritmética de los precios con `statistics.mean()`.
- `pathlib`: construye la ruta del archivo de la base de datos.
- `contextlib`: permite asegurar el cierre de las conexiones con `closing()`.

Todos son módulos de la biblioteca estándar de Python. No se requiere instalar paquetes externos ni utilizar `pip`.

## Cómo ejecutar

1. Descarga o clona el repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:

```bash
python main.py
```

En algunos equipos puedes necesitar `python3 main.py`.

En la primera ejecución se crea `catalogo.db` y la tabla `productos`. Los registros permanecen guardados para ejecuciones posteriores.

## Cómo probar

1. Selecciona la opción **1** y registra al menos cinco productos.
2. Selecciona **2** para consultar los registros.
3. Selecciona **3** para calcular el promedio de los precios.
4. Intenta registrar un nombre vacío y un precio negativo.
5. Para probar el catálogo vacío, cierra el programa y elimina `catalogo.db` con el programa detenido. Al volver a ejecutar se crea una base nueva. Hazlo solo si no necesitas conservar tus datos.

## Evidencias

Guarda en `evidencias/` capturas obtenidas al ejecutar el programa:

- `productos_registrados.png`: catálogo con al menos cinco productos.
- `promedio_calculado.png`: resultado del promedio.
- Puedes añadir capturas de las validaciones y del catálogo vacío.

Las capturas deben ser resultados reales de la ejecución, no imágenes simuladas.
