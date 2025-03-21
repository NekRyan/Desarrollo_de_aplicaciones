import streamlit as st
import os
from supabase import create_client, Client

#configurar supabase

SUPABASE_URL = "https://bmuksajpluhszplulsvv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtdWtzYWpwbHVoc3pwbHVsc3Z2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU1MDIsImV4cCI6MjA1NzMyMTUwMn0.FxisTKSWk17XsI3E9oypN9MFRfVHSDuERcXz2zDcECg"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Gesti[on de Clientes CRUD Supabase y Streamlit]")

#Formulario agregar cliente

st.header("Agregar Cliente")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
telefono = st.text_input("Telefono")

if st.button("Agregar Cliente"):
    if nombre and email:
        data = {"nombre": nombre, "email": email, "telefono": telefono}
        response = supabase.table("clientes").insert(data).execute()
        st.success("Clientes agregados correctamente")
    else: 
        st.warning("Nombre y Email son obligatorios")