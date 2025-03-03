import streamlit as st

# Clase base para todos los empleados
class Empleado:
    def __init__(self, nombre, cargo, jefe=None, estado="Activo"):
        self.nombre = nombre
        self.cargo = cargo
        self.jefe = jefe
        self.estado = estado  # Activo por defecto

    def get_resumen(self):
        return f"{self.nombre} - {self.cargo}"

    def get_jefe_inmediato(self):
        return self.jefe.nombre if self.jefe else "No tiene jefe"

    def get_estado(self):
        if self.estado in ["TC", "D", "R"]:
            return f"Estado: {self.estado}"
        return "Activo"

    # Métodos Getter y Setter para estado
    def set_estado(self, nuevo_estado):
        if nuevo_estado in ["TC", "D", "R", "Activo"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido. Usa: TC, D, R o Activo.")

# Creación de empleados
gerente = Empleado("Carlos López", "Gerente")
jefe_marketing = Empleado("María Pérez", "Jefe de Marketing", gerente)
asistente_marketing = Empleado("Ana Gómez", "Asistente", jefe_marketing)
tecnico1 = Empleado("Luis Torres", "Técnico", jefe_marketing, "D")  # Despedido

# Mostrar en Streamlit
st.title("Sistema de Gestión de Recursos Humanos")

empleados = [gerente, jefe_marketing, asistente_marketing, tecnico1]

for emp in empleados:
    st.write(f"👤 {emp.get_resumen()}")
    st.write(f"👨‍💼 Jefe inmediato: {emp.get_jefe_inmediato()}")
    st.write(f"📌 {emp.get_estado()}")
    st.write("---")

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