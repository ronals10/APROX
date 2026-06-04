import streamlit as st
import sqlite3
import pandas as pd

from db import init_db, insertar_lamparas

init_db()
insertar_lamparas()

st.set_page_config(
    page_title="Luces Aproximación",
    layout="wide"
)

st.title("Sistema de Gestión de Luces de Aproximación")

conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM lamparas",
    conn
)

total = len(df)
operativas = len(df[df.estado=="Operativa"])
inoperativas = len(df[df.estado=="Inoperativa"])

disp = round(
    (operativas/total)*100,
    2
)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Total",total)
c2.metric("Operativas",operativas)
c3.metric("Inoperativas",inoperativas)
c4.metric("Disponibilidad",f"{disp}%")

st.divider()

st.subheader("Estado de lámparas")

st.dataframe(
    df,
    use_container_width=True
)
