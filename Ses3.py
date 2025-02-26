import streamlit as st

#Funcion para clasificar puntaje
def clasificar_puntaje(puntaje):
    if puntaje >= 85:
        return "Excelente"
    elif puntaje >= 70:
        return "Bueno"
    else:
        return "Necesita Mejorar"

#Menú Lateral
st.sidebar.title("Menú de navegación")
opcion = st.sidebar._selectbox("Seleccione una opción", ["Inicio", "Clasificación de Puntajes"])

#Sección: Inicio
if opcion == "Inicio":
    st.title("Bienvenido a la Aplicación")
    st.write("Mueva el deslizador para como se clasifica el puntaje en tiempo real")
    
    #Filtro desplazable
    puntaje_slider = st.slider("Seleccione un puntaje:", 0, 100, 50)

    #Mostrar la clasificacion en tiempo real
    st.info(f"El puntaje {puntaje_slider} es clasificado como: **{clasificar_puntaje(puntaje_slider)}**")


#Sección: Clasificacion de Puntajes
elif opcion == "Clasificacion de Puntajes":
    st.title("Clasificacion de Puntajes") 
    st.write("Ingrese un puntaje y el sistema lo clasificará.") 

    #Entrada de usuario
    puntaje = st.number_input("Ingrese un puntaje (0-100):", min_value=0, max_value=100, step=1)

    #Boton para clasificar
    if st.button("Clasificar"):
        resultado = clasificar_puntaje(puntaje)
        st.success(f"El puntaje {puntaje} es clasficado como: {resultado}")

