import streamlit as st

import streamlit as st

# Clase base para todos los empleados
class Empleado:
    def __init__(self, nombre, puesto, estado="Activo"):
        self.nombre = nombre
        self.puesto = puesto
        self.estado = estado
    
    def def_resumen(self):
        return f"{self.nombre} - {self.puesto}"
    
    def def_estado(self):
        return self.estado

# Clase para Gerente
class Gerente(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Gerente")
    
    def def_jefe_inmediato(self):
        return "No tiene jefe inmediato"

# Clase para Jefe de Área
class JefeArea(Empleado):
    def __init__(self, nombre, gerente):
        super().__init__(nombre, "Jefe de Área")
        self.gerente = gerente
    
    def def_jefe_inmediato(self):
        return self.gerente.nombre

# Clase para Asistentes
class Asistente(Empleado):
    def __init__(self, nombre, jefe):
        super().__init__(nombre, "Asistente")
        self.jefe = jefe
    
    def def_jefe_inmediato(self):
        return self.jefe.nombre

# Clase para Técnicos
class Tecnico(Empleado):
    def __init__(self, nombre, jefe, experiencia):
        super().__init__(nombre, "Técnico")
        self.jefe = jefe
        self.experiencia = experiencia
    
    def def_resumen(self):
        return f"{self.nombre} - {self.puesto} con {self.experiencia} años de experiencia"
    
    def def_jefe_inmediato(self):
        return self.jefe.nombre

# Creación de empleados
gerente = Gerente("Carlos Pérez")
jefes = [JefeArea(f"Jefe {i+1}", gerente) for i in range(5)]
asistentes = [Asistente(f"Asistente {i+1}", jefes[i//2]) for i in range(10)]
tecnicos = [Tecnico(f"Técnico {i+1}", jefes[i//5], i+1) for i in range(20)]

empleados = [gerente] + jefes + asistentes + tecnicos

# Interfaz con Streamlit
st.title("Sistema de Gestión de Empleados")
for emp in empleados:
    st.write(emp.def_resumen())
    st.write(f"Jefe inmediato: {emp.def_jefe_inmediato()}")
    st.write(f"Estado: {emp.def_estado()}")
    st.write("---")