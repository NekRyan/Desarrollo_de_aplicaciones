import streamlit as st
from supabase import create_client, client
import os

#configurar supabase

SUPABASE_URL = "https://bmuksajpluhszplulsvv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtdWtzYWpwbHVoc3pwbHVsc3Z2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU1MDIsImV4cCI6MjA1NzMyMTUwMn0.FxisTKSWk17XsI3E9oypN9MFRfVHSDuERcXz2zDcECg"
supabase: client = create_client(SUPABASE_KEY, SUPABASE_URL)

st.title("Gestion de clientes - CRUD con Supabase y Streamlit")

#Formulario para agregar cliente

st.header("Agregar cliente")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
telefono = st.text_input("Telefono")

if st.button("Agregar cliente"):
    if nombre and email:
        data = {"nombre": nombre, "email": email, "telefono": telefono}
        response = supabase.table("Clientes").insert(data).execute()
        st.success("Cliente satisfecho correctamente")
    
    else:
        st.warning("Nombre y email son obligatorios")


st.header("Clientes registrados")
#Obtener a los clientes
clientes = supabase.table("clientes").select("*").execute()
if clientes.data:
    for cliente in clientes.data:
        st.subheader(cliente["nombre"])
        st.write(f"{cliente['email']}")
        st.write(f"{cliente['telefono']}")
        st.write(f"Fecha de registro: {cliente['fecha_registro']}")
    
    else:
        st.info("No hay clientes registrador aun")
