import streamlit as st

def validar_producto(nombre, precio, categorias, en_venta):
    categorias_validas = ["Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"]
    
    # Validaciones
    if len(nombre) > 20:
        return "Lo sentimos no pudo crear este producto. El nombre del producto no debe superar los 20 caracteres."
    
    try:
        precio = float(precio)
        if precio <= 0 or precio >= 999:
            return "Lo sentimos no pudo crear este producto. El precio debe estar entre 0 y 999 soles."
    except ValueError:
        return "Lo sentimos no pudo crear este producto. Por favor verifique el campo del precio."
    
    i = 0
    while i < len(categorias):
        if categorias[i] not in categorias_validas:
            return "Lo sentimos no pudo crear este producto. Una de las categorías seleccionadas no es válida."
        i += 1
    
    if en_venta not in ["Sí", "No"]:
        return "Lo sentimos no pudo crear este producto. Debe seleccionar si el producto está en venta."
    
    return "Felicidades, su producto se agregó."

def main():
    st.title("Registro de Productos - Confitería Dulcino")
    
    nombre = st.text_input("Nombre del Producto:")
    precio = st.text_input("Precio del Producto:")
    categorias = st.multiselect("Categorías del Producto:", ["Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"])
    en_venta = st.radio("¿El producto está en venta?", ["Sí", "No"])
    
    if st.button("Registrar Producto"):
        mensaje = validar_producto(nombre, precio, categorias, en_venta)
        st.write(mensaje)

if __name__ == "__main__":
    main()
