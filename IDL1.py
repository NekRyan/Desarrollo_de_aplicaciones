import streamlit as st

class Empleado:
    def __init__(self, nombre, cargo, jefe=None, estado="Activo"):
        self.nombre = nombre
        self.cargo = cargo
        self.jefe = jefe
        self.estado = estado  # Activo por defecto

    def get_resumen(self):
        """Retorna el nombre del trabajador junto con su cargo."""
        return f"{self.nombre} - {self.cargo}"

    def get_jefe_inmediato(self):
        """Retorna el jefe inmediato del trabajador o 'No tiene jefe' si es gerente."""
        return self.jefe.nombre if self.jefe else "No tiene jefe"

    def get_estado(self):
        """Retorna el estado del empleado (Activo, TC, D, R)."""
        return f"Estado: {self.estado}" if self.estado in ["TC", "D", "R"] else "Activo"

    # Métodos Getter y Setter
    def set_estado(self, nuevo_estado):
        if nuevo_estado in ["TC", "D", "R", "Activo"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido. Usa: TC, D, R o Activo.")

class Tecnico(Empleado):
    def __init__(self, nombre, jefe, experiencia, estado="Activo"):
        super().__init__(nombre, "Técnico", jefe, estado)
        self.experiencia = experiencia  # Años de experiencia

    def get_resumen(self):
        """Retorna el nombre, cargo y años de experiencia del técnico."""
        return f"{self.nombre} - {self.cargo} ({self.experiencia} años de experiencia)"

# Creación de empleados
gerente = Empleado("Carlos López", "Gerente")
jefe_marketing = Empleado("María Pérez", "Jefe de Marketing", gerente)
asistente_marketing = Empleado("Ana Gómez", "Asistente", jefe_marketing)
tecnico1 = Tecnico("Luis Torres", jefe_marketing, 5, "D")  # Despedido
tecnico2 = Tecnico("Pedro Rojas", jefe_marketing, 3)

# Mostrar en Streamlit
st.title("📊 Sistema de Gestión de Recursos Humanos")

empleados = [gerente, jefe_marketing, asistente_marketing, tecnico1, tecnico2]

for emp in empleados:
    st.write(f"👤 {emp.get_resumen()}")
    st.write(f"👨‍💼 Jefe inmediato: {emp.get_jefe_inmediato()}")
    st.write(f"📌 {emp.get_estado()}")
    st.write("---")
