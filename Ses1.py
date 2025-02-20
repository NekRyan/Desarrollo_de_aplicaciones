import streamlit as st

#Titulo de la aplicacion
st.title("Bievenido a mi aplicación")

#Solicitar nombre de usuario
nombre = st.text_input("Por favor ingrese su nombre")

#Mostrar saludo si el usuario ingresa su nombre
if nombre:
    st.write(f"Hola, {nombre}! Bievenido a esta aplicación web de streamlit")