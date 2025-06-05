import sqlite3
from datetime import datetime

DB = "biblioteca.db"

def crear_tabla():
    
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestamos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                inventario TEXT,
                titulo TEXT,
                fecha_prestamo TEXT,
                fecha_devolución TEXT,
                devuelto TEXT
            )
                    """)
        conn.commit()
        print("✅ Tabla creada o ya existente")