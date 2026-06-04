import streamlit as st
import sqlite3
import pandas as pd

st.title("Historial")

conn = sqlite3.connect(
    "database.db"
)

df = pd.read_sql(
    """
    SELECT *
    FROM mantenimientos
    ORDER BY fecha DESC
    """,
    conn
)

st.dataframe(
    df,
    use_container_width=True
)
