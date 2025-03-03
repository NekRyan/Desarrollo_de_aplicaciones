import streamlit as st

class Empleado:
    def __init__(self, nombre, cargo, jefe=None, estado="Activo"):
        self._nombre = nombre
        self._cargo = cargo
        self._jefe = jefe
        self._estado = estado

    # Métodos Getter y Setter
    def get_nombre(self):
        return self._nombre

    def get_cargo(self):
        return self._cargo

    def get_jefe(self):
        return self._jefe.get_nombre() if self._jefe else "No tiene jefe"

    def get_estado(self):
        return self._estado

    def resumen(self):
        return f"{self._nombre} - {self._cargo}"

    def jefe_inmediato(self):
        return self.get_jefe()

    def estado(self):
        estados = {"TC": "🟠 Término de Contrato", "D": "🔴 Despedido", "R": "🟡 Renuncia", "Activo": "🟢 Activo"}
        return estados.get(self._estado, "🟢 Activo")


class Tecnico(Empleado):
    def __init__(self, nombre, jefe, experiencia, estado="Activo"):
        super().__init__(nombre, "Técnico", jefe, estado)
        self._experiencia = experiencia

    def resumen(self):
        return f"{self._nombre} - {self._cargo} ({self._experiencia} años de experiencia)"


class JefeArea(Empleado):
    def __init__(self, nombre, area, gerente, estado="Activo"):
        super().__init__(nombre, f"Jefe de {area}", gerente, estado)
        self._area = area
        self._asistentes = []
        self._tecnicos = []

    def agregar_asistente(self, asistente):
        if len(self._asistentes) < 2:
            self._asistentes.append(asistente)

    def agregar_tecnico(self, tecnico):
        if len(self._tecnicos) < 5:
            self._tecnicos.append(tecnico)


class Asistente(Empleado):
    def __init__(self, nombre, jefe, estado="Activo"):
        super().__init__(nombre, "Asistente", jefe, estado)


# 📌 CREACIÓN DE EMPLEADOS
gerente = Empleado("Carlos López", "Gerente")

jefe_marketing = JefeArea("María Pérez", "Marketing", gerente)
jefe_sistemas = JefeArea("Juan Torres", "Sistemas", gerente)
jefe_produccion = JefeArea("Laura Gómez", "Producción", gerente)
jefe_logistica = JefeArea("Miguel Rojas", "Logística", gerente)

asistente1 = Asistente("Ana Gómez", jefe_marketing)
asistente2 = Asistente("Pedro Núñez", jefe_sistemas)

tecnico1 = Tecnico("Luis Torres", jefe_marketing, 5, "D")
tecnico2 = Tecnico("Sofía Herrera", jefe_sistemas, 3)
tecnico3 = Tecnico("Andrés Ramírez", jefe_produccion, 4)
tecnico4 = Tecnico("Daniela Pérez", jefe_logistica, 2)
tecnico5 = Tecnico("Mario López", jefe_marketing, 6)

jefe_marketing.agregar_asistente(asistente1)
jefe_sistemas.agregar_asistente(asistente2)

jefe_marketing.agregar_tecnico(tecnico1)
jefe_marketing.agregar_tecnico(tecnico5)
jefe_sistemas.agregar_tecnico(tecnico2)
jefe_produccion.agregar_tecnico(tecnico3)
jefe_logistica.agregar_tecnico(tecnico4)

# 📌 LISTA DE EMPLEADOS
empleados = [gerente, jefe_marketing, jefe_sistemas, jefe_produccion, jefe_logistica,
             asistente1, asistente2, tecnico1, tecnico2, tecnico3, tecnico4, tecnico5]

# 📌 INTERFAZ MEJORADA EN STREAMLIT
st.set_page_config(page_title="Gestión de Recursos Humanos", page_icon="📊")

st.title("📊 Gestión de Recursos Humanos")
st.write("Sistema de visualización interactivo para la jerarquía de empleados.")

# 📌 FILTROS INTERACTIVOS
tipo_empleado = st.selectbox("🔍 Filtrar por tipo de empleado:", ["Todos", "Gerente", "Jefe de Área", "Asistente", "Técnico"])
buscar_nombre = st.text_input("🔎 Buscar por nombre:")

# 📌 MOSTRAR EMPLEADOS SEGÚN FILTRO
for emp in empleados:
    if tipo_empleado != "Todos" and tipo_empleado not in emp.get_cargo():
        continue
    if buscar_nombre and buscar_nombre.lower() not in emp.get_nombre().lower():
        continue

    with st.expander(f"👤 {emp.resumen()}"):
        st.write(f"**👨‍💼 Jefe inmediato:** {emp.jefe_inmediato()}")
        st.write(f"**📌 Estado:** {emp.estado()}")

