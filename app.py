import streamlit as st

# Título de la aplicación
st.title("Mi Primera App con Streamlit 🚀")

# Entrada de texto
name = st.text_input("¿Cuál es tu nombre?")

# Mostrar mensaje
if name:
    st.write(f"Hola, {name}! Bienvenido a Streamlit.")
