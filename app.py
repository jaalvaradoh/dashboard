# app.py
import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(
    page_title="Ecuaciones de Primer Grado",
    page_icon="🧮",
    layout="centered"
)

# Inicializar variables de sesión
if "a" not in st.session_state:
    st.session_state.a = 1

if "b" not in st.session_state:
    st.session_state.b = 1

if "x" not in st.session_state:
    st.session_state.x = 1

if "generated" not in st.session_state:
    st.session_state.generated = False


# Función para generar nueva ecuación
def generar_ecuacion():
    x = random.randint(1, 10)  # Respuesta entre 1 y 10
    a = random.randint(1, 10)
    b = random.randint(1, 20)

    st.session_state.a = a
    st.session_state.b = b
    st.session_state.x = x
    st.session_state.generated = True


# Título
st.title("🧮 Practica Ecuaciones de Primer Grado")
st.write("Resuelve la ecuación y encuentra el valor de x.")

# Botón para generar nueva pregunta
if st.button("🎲 Generar Nueva Pregunta"):
    generar_ecuacion()

# Generar automáticamente la primera vez
if not st.session_state.generated:
    generar_ecuacion()

# Construcción de ecuación
a = st.session_state.a
b = st.session_state.b
x = st.session_state.x

resultado = a * x + b

# Mostrar ecuación
st.markdown(
    f"""
    <div style="
        font-size:40px;
        text-align:center;
        padding:20px;
        border-radius:15px;
        background-color:#f0f2f6;
        margin-bottom:20px;
    ">
        {a}x + {b} = {resultado}
    </div>
    """,
    unsafe_allow_html=True
)

# Entrada del usuario
respuesta = st.number_input(
    "Ingresa el valor de x:",
    min_value=0,
    max_value=20,
    step=1
)

# Botón verificar
if st.button("✅ Verificar Respuesta"):

    if respuesta == x:
        st.success("🎉 ¡Correcto! Excelente trabajo.")

        # Animación
        st.balloons()

        # Mensaje animado
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        st.markdown(
            """
            <h2 style='text-align:center; color:green;'>
            ⭐ ¡Has resuelto la ecuación correctamente! ⭐
            </h2>
            """,
            unsafe_allow_html=True
        )

    else:
        st.error("❌ Respuesta incorrecta. Inténtalo nuevamente.")

        pista = (resultado - b) // a

        st.info(f"💡 Pista: despeja x usando (resultado - {b}) ÷ {a}")
