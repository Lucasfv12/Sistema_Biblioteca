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

def registrar_prestamo():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    inventario = input("N° inventario: ")
    titulo = input("Titulo del libro: ")
    fecha_prestamo = datetime.today().strftime("%Y-%m-%d")
    fecha_devolucion = input("Fecha de devolución esperada (YYYY-MM-DD): ")
    
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                    INSERT INTO prestamos (nombre, apellido, inventario, titulo, fecha_prestamo, fecha_devolucion, devuelto)
                    VALUES (?, ?, ?, ?, ?, ?, 'no')
                    """, (nombre, apellido, inventario, titulo, fecha_prestamo, fecha_devolucion,))
        conn.commit()
        print("✅ Préstamo registrado.")
        
def ver_prestamos():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prestamos")
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
            

def ver_vencidos():
        hoy = datetime.today().date()
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                        SELECT * FROM prestamos WHERE devueltos='no'""")
            filas = cursor.fetchall()
            for f in filas:
                devolucion = datetime.strftime(f[6], "%Y-%m-%d").date()
                if devolucion < hoy:
                    print(f"⚠️ Vencido: {f}")