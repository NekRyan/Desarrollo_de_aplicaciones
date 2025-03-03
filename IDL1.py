import streamlit as st

class Empleado:
    def __init__(self, nombre, cargo, jefe=None, estado="Activo"):
        self.nombre = nombre
        self.cargo = cargo
        self.jefe = jefe
        self.estado = estado  

    def resumen(self):
        """Retorna el nombre del trabajador junto con su cargo."""
        return f"{self.nombre} - {self.cargo}"

    def jefe_inmediato(self):
        """Retorna el jefe inmediato del trabajador o 'No tiene jefe' si es gerente."""
        return self.jefe.nombre if self.jefe else "No tiene jefe"

    def estado(self):
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
        self.experiencia = experiencia 

    def resumen(self):
        """Retorna el nombre, cargo y años de experiencia del técnico."""
        return f"{self.nombre} - {self.cargo} ({self.experiencia} años de experiencia)"

class JefeArea(Empleado):
    def __init__(self, nombre, area, gerente, estado="Activo"):
        super().__init__(nombre, f"Jefe de {area}", gerente, estado)
        self.area = area
        self.asistentes = []
        self.tecnicos = []

    def agregar_asistente(self, asistente):
        """Agrega asistentes al jefe de área (máximo 2)."""
        if len(self.asistentes) < 2:
            self.asistentes.append(asistente)
        else:
            raise ValueError(f"El área {self.area} ya tiene el máximo de 2 asistentes.")

    def agregar_tecnico(self, tecnico):
        """Agrega técnicos al jefe de área (máximo 5)."""
        if len(self.tecnicos) < 5:
            self.tecnicos.append(tecnico)
        else:
            raise ValueError(f"El área {self.area} ya tiene el máximo de 5 técnicos.")

class Asistente(Empleado):
    def __init__(self, nombre, jefe, estado="Activo"):
        super().__init__(nombre, "Asistente", jefe, estado)

# Creación de empleados según la jerarquía
gerente = Empleado("Carlos López", "Gerente")

# Creación de jefes de área
jefe_marketing = JefeArea("María Pérez", "Marketing", gerente)
jefe_sistemas = JefeArea("Juan Torres", "Sistemas", gerente)
jefe_produccion = JefeArea("Laura Gómez", "Producción", gerente)
jefe_logistica = JefeArea("Miguel Rojas", "Logística", gerente)

# Creación de asistentes y técnicos
asistente1 = Asistente("Ana Gómez", jefe_marketing)
asistente2 = Asistente("Pedro Núñez", jefe_sistemas)

tecnico1 = Tecnico("Luis Torres", jefe_marketing, 5, "D") 
tecnico2 = Tecnico("Sofía Herrera", jefe_sistemas, 3)
tecnico3 = Tecnico("Andrés Ramírez", jefe_produccion, 4, "D") 
tecnico4 = Tecnico("Daniela Pérez", jefe_logistica, 2)
tecnico5 = Tecnico("Mario López", jefe_marketing, 6)

# Asignación de subordinados
jefe_marketing.agregar_asistente(asistente1)
jefe_sistemas.agregar_asistente(asistente2)

jefe_marketing.agregar_tecnico(tecnico1)
jefe_marketing.agregar_tecnico(tecnico5)
jefe_sistemas.agregar_tecnico(tecnico2)
jefe_produccion.agregar_tecnico(tecnico3)
jefe_logistica.agregar_tecnico(tecnico4)

# For Streamlit
st.title("📊 Sistema de Gestión de Recursos Humanos")

empleados = [gerente, jefe_marketing, jefe_sistemas, jefe_produccion, jefe_logistica,
             asistente1, asistente2, tecnico1, tecnico2, tecnico3, tecnico4, tecnico5]

for emp in empleados:
    st.write(f"👤 {emp.get_resumen()}")
    st.write(f"👨‍💼 Jefe inmediato: {emp.get_jefe_inmediato()}")
    st.write(f"📌 {emp.get_estado()}")
    st.write("---")
