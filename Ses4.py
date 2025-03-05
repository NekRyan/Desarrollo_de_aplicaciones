import streamlit as st

st.title("Estrucuturas de controles repetitivas")

#Entrada del usuario para limite de bucle
limite = st.number_input("Ingrese numero limite para los bucles: ", min_value=1, step=1)

st.subheader("Bucle FOR")

for i in range(1, limite + 1):
    st.write(f"Iteraci[on {i} con for")

st.subheader ("Bucle While")
contador = 1

while contador <= limite:
    st.write(f"Iteracion {contador} con while")
    contador += 1