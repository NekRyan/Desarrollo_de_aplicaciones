import streamlit as st
from algoritmos import AlgoritmosSecuenciales

st.title("Algoritmos secuenciales con POO Streamlit")

#entrada de usuario
numero = st.number_input("Ingrese un numero entero positivo", min_value=1, value=5, step=1)

#Instanciamos la clase con el numero ingresado
algoritmos = AlgoritmosSecuenciales(numero)

#Crear botones para ejecutar los algoritmos secunciales
if st.button("Calcular suma de N numeros"):
    st.success(f"La suma de los primeros {numero} numero es: {algoritmos.suma_n_numeros()}")

if st.button("Calcular factorial"):
    st.success(f"el factorial de {numero} es: {algoritmos.factorial()}")

if st.button("Generar secuencia de fibonacci"):
    st.success(f"la secuencia de Fibonacci con {numero} terminos es: {algoritmos.fibonacci()}")