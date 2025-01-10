import os

if "VERCEL" in os.environ:
    import streamlit.web.bootstrap
    import sys

    sys.argv = ["streamlit", "run", "app.py", "--server.headless", "true", "--server.port", os.environ.get("PORT", "8501")]
    sys.exit(streamlit.web.bootstrap.run())

import streamlit as st

# Título de la aplicación
st.title("Mi Primera App con Streamlit 🚀")

# Entrada de texto
name = st.text_input("¿Cuál es tu nombre?")

# Mostrar mensaje
if name:
    st.write(f"Hola, {name}! Bienvenido a Streamlit.")

# Gráfica de ejemplo
import pandas as pd
import numpy as np

st.subheader("Gráfica de ejemplo")
data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["X", "Y"]
)
st.line_chart(data)
