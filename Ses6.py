import streamlit as st
import os
from supabase import create_client, Client

#configurar supabase

SUPABASE_URL = "https://bmuksajpluhszplulsvv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtdWtzYWpwbHVoc3pwbHVsc3Z2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU1MDIsImV4cCI6MjA1NzMyMTUwMn0.FxisTKSWk17XsI3E9oypN9MFRfVHSDuERcXz2zDcECg"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Registro de Clientes")

#Formulario agregar cliente

st.header("Agregar Cliente")
nombre = st.text_input("Nombre")
email = st.text_input("Email")
telefono = st.text_input("Telefono")
ciudad = st.text_input("Ciudad")
direccion = st.text_input("Dirección")
foto = st.file_uploader("Subir foto", type=["jpg", "png", "jpeg"])

if st.button("Agregar Cliente"):
    if nombre and email:
        foto_url = None
        if foto:
            foto_bytes = foto.read()
            file_path = f"clientes/{nombre}_{email}.jpg"
            supabase.storage.from_("fotos_clientes").upload(file_path, BytesIO(foto_bytes), {"content-type": "image/jpeg"})
            foto_url = f"{SUPABASE_URL}/storage/v1/object/public/fotos_clientes/{file_path}"

        data = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono,
            "ciudad": ciudad,
            "direccion": direccion,
            "foto_url": foto_url
        }
        response = supabase.table("clientes").insert(data).execute()
        st.success("Cliente agregado correctamente")
    else:
        st.warning("Nombre y Email son obligatorios")
   