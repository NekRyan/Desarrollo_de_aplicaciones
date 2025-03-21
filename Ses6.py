import streamlit as st
from supabase import create_client, Client

# Configurar Supabase
SUPABASE_URL = "https://bmuksajpluhszplulsvv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtdWtzYWpwbHVoc3pwbHVsc3Z2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU1MDIsImV4cCI6MjA1NzMyMTUwMn0.FxisTKSWk17XsI3E9oypN9MFRfVHSDuERcXz2zDcECg"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Registro de Clientes")

# Formulario para agregar cliente
st.header("Agregar Cliente")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
telefono = st.text_input("Teléfono")
ciudad = st.text_input("Ciudad")
direccion = st.text_input("Dirección")

if st.button("Agregar Cliente"):
    if nombre and email:
        try:
            data = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono,
                "ciudad": ciudad,
                "direccion": direccion
            }
            response = supabase.table("clientes").insert(data).execute()

            # Acceder correctamente a la respuesta de Supabase
            if response.data:
                st.success("Cliente agregado correctamente")
            elif response.error:
                st.error(f"Error al registrar el cliente: {response.error.message}")
            else:
                st.error("Error desconocido al registrar el cliente")

        except Exception as e:
            st.error(f"Error en la base de datos: {e}")
    else:
        st.warning("Nombre y Email son obligatorios")
