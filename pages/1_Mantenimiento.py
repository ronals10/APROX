import streamlit as st
import sqlite3
from datetime import datetime
import os

st.title("Registro de Mantenimiento")

conn = sqlite3.connect("database.db")

lamparas = conn.execute(
    "SELECT codigo FROM lamparas"
).fetchall()

lamparas = [x[0] for x in lamparas]

codigo = st.selectbox(
    "Lámpara",
    lamparas
)

tipo = st.selectbox(
    "Tipo",
    [
        "Preventivo",
        "Correctivo"
    ]
)

descripcion = st.text_area(
    "Descripción"
)

foto = st.file_uploader(
    "Fotografía",
    type=["jpg","png","jpeg"]
)

if st.button("Guardar"):

    ruta = ""

    if foto:

        os.makedirs(
            "uploads",
            exist_ok=True
        )

        ruta = f"uploads/{foto.name}"

        with open(ruta,"wb") as f:
            f.write(foto.read())

    conn.execute("""
    INSERT INTO mantenimientos
    (
    fecha,
    codigo_lampara,
    tipo,
    descripcion,
    foto
    )
    VALUES
    (?,?,?,?,?)
    """,
    (
    datetime.now().strftime("%Y-%m-%d"),
    codigo,
    tipo,
    descripcion,
    ruta
    ))

    conn.commit()

    st.success("Registro guardado")
