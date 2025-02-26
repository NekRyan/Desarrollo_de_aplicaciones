import streamlit as st

#Funcion para clasificar puntaje
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "Excelente"
    elif puntaje >= 70:
        return "Bueno"
    else:
        return "Necesita Mejorar"

#Interfaz en Streamlit
st.title("Clasificacion de Puntajes") 
st.title("Ingrese un puntaje y el sistema lo clasificará") 

#Entrada de usuario
puntaje = st.number_input("Ingrese un puntaje (0-100):", min_value=0, max_value=100, step=1)

#Boton para clasificar
if st.button("Clasificar"):
    resultado = clasificar_puntaje(puntaje)
    st.success(f"El puntaje {puntaje} es clasficado como: {resultado}")

