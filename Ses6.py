import streamlit as st
from supabase import create_client, Client
from io import BytesIO

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
foto = st.file_uploader("Subir foto", type=["jpg", "png", "jpeg"])

if st.button("Agregar Cliente"):
    if nombre and email:
        foto_url = None

        if foto:
            try:
                foto_bytes = foto.read()
                file_path = f"clientes/{nombre}_{email}.jpg"

                # Subir imagen a Supabase Storage
                response = supabase.storage.from_("fotosclientes").upload(
                    file_path, BytesIO(foto_bytes), {"content-type": "image/jpeg"}
                )

                # Verificar si la imagen se subió correctamente
                if not response.error:
                    foto_url = f"{SUPABASE_URL}/storage/v1/object/public/fotosclientes/{file_path}"
                else:
                    st.error(f"Error al subir la imagen: {response.error}")
            except Exception as e:
                st.error(f"Error al subir la imagen: {e}")

        # Insertar datos en Supabase
        try:
            data = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono,
                "ciudad": ciudad,
                "direccion": direccion,
                "foto_url": foto_url,  # Corrección del nombre de la clave
            }
            response = supabase.table("clientes").insert(data).execute()

            if not response.error:
                st.success("Cliente agregado correctamente")
            else:
                st.error(f"Error al registrar el cliente: {response.error}")
        except Exception as e:
            st.error(f"Error en la base de datos: {e}")
    else:
        st.warning("Nombre y Email son obligatorios")