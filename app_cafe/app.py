import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------
st.set_page_config(
    page_title="Predicción de Calidad de Café",
    page_icon="☕",
    layout="wide"
)

# ---------------------------------------------------
# CARGA DEL MODELO
# ---------------------------------------------------
@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_cafe.pkl")

modelo = cargar_modelo()

# ---------------------------------------------------
# ESTILOS COLOR CAFÉ
# ---------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #F5EFE6;
    }

    .main {
        padding-top: 1rem;
    }

    .titulo-principal {
        font-size: 2.3rem;
        font-weight: 700;
        color: #4E342E;
        margin-bottom: 0.2rem;
    }

    .subtitulo {
        font-size: 1.05rem;
        color: #6D4C41;
        margin-bottom: 1.2rem;
    }

    .caja-info {
        background-color: #FFF8F2;
        padding: 1rem;
        border-radius: 14px;
        border-left: 6px solid #6D4C41;
        border: 1px solid #E0CFC2;
        margin-bottom: 1rem;
    }

    .resultado-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 14px;
        border-left: 6px solid #2E7D32;
        border: 1px solid #C8E6C9;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .firma {
        text-align: center;
        color: #6D4C41;
        font-size: 0.95rem;
        margin-top: 2rem;
        padding: 15px;
        background-color: #FFF8F2;
        border-radius: 12px;
        border: 1px solid #E0CFC2;
    }

    .stButton > button {
        background-color: #6D4C41;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-weight: 600;
        border: none;
    }

    .stButton > button:hover {
        background-color: #4E342E;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #EFE4D6;
    }

    div[data-testid="stMetric"] {
        background-color: #FFF8F2;
        border: 1px solid #E0CFC2;
        padding: 10px;
        border-radius: 10px;
    }

    div.stExpander {
        background-color: #FFF8F2;
        border-radius: 10px;
    }

    .bloque-categoria {
        background-color: #FFF8F2;
        border: 1px solid #D7C3B5;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# FUNCIONES AUXILIARES
# ---------------------------------------------------
def cargar_ejemplo(tipo):
    if tipo == "Comercial":
        st.session_state.aroma = 6.2
        st.session_state.flavor = 6.3
        st.session_state.aftertaste = 6.1
        st.session_state.acidity = 6.2
        st.session_state.body = 6.3
        st.session_state.balance = 6.2
        st.session_state.uniformity = 7.0
        st.session_state.clean_cup = 7.0
        st.session_state.sweetness = 7.0
        st.session_state.overall = 6.1
        st.session_state.moisture = 0.13

    elif tipo == "Bueno":
        st.session_state.aroma = 7.0
        st.session_state.flavor = 7.1
        st.session_state.aftertaste = 7.0
        st.session_state.acidity = 7.0
        st.session_state.body = 7.0
        st.session_state.balance = 7.0
        st.session_state.uniformity = 8.0
        st.session_state.clean_cup = 8.0
        st.session_state.sweetness = 8.0
        st.session_state.overall = 7.0
        st.session_state.moisture = 0.12

    elif tipo == "Muy bueno":
        st.session_state.aroma = 7.8
        st.session_state.flavor = 7.9
        st.session_state.aftertaste = 7.7
        st.session_state.acidity = 7.8
        st.session_state.body = 7.7
        st.session_state.balance = 7.8
        st.session_state.uniformity = 8.5
        st.session_state.clean_cup = 8.5
        st.session_state.sweetness = 8.5
        st.session_state.overall = 7.8
        st.session_state.moisture = 0.12

    elif tipo == "Excelente":
        st.session_state.aroma = 8.7
        st.session_state.flavor = 8.8
        st.session_state.aftertaste = 8.6
        st.session_state.acidity = 8.7
        st.session_state.body = 8.6
        st.session_state.balance = 8.7
        st.session_state.uniformity = 10.0
        st.session_state.clean_cup = 10.0
        st.session_state.sweetness = 10.0
        st.session_state.overall = 8.8
        st.session_state.moisture = 0.11


def interpretar_valor(valor):
    if valor >= 8.5:
        return "Muy alto"
    elif valor >= 7.5:
        return "Alto"
    elif valor >= 6.5:
        return "Medio"
    else:
        return "Bajo"


def mostrar_tarjeta_resumen(nombre, valor):
    etiqueta = interpretar_valor(valor)
    st.metric(label=nombre, value=f"{valor:.2f}", delta=etiqueta)


def color_categoria(categoria):
    categoria = str(categoria).strip().lower()
    if categoria == "excelente":
        return "#2E7D32"
    elif categoria == "muy bueno":
        return "#558B2F"
    elif categoria == "bueno":
        return "#EF6C00"
    elif categoria == "comercial":
        return "#8D6E63"
    return "#6D4C41"


# ---------------------------------------------------
# VALORES INICIALES
# ---------------------------------------------------
if "aroma" not in st.session_state:
    st.session_state.aroma = 8.0
if "flavor" not in st.session_state:
    st.session_state.flavor = 8.0
if "aftertaste" not in st.session_state:
    st.session_state.aftertaste = 8.0
if "acidity" not in st.session_state:
    st.session_state.acidity = 8.0
if "body" not in st.session_state:
    st.session_state.body = 8.0
if "balance" not in st.session_state:
    st.session_state.balance = 8.0
if "uniformity" not in st.session_state:
    st.session_state.uniformity = 10.0
if "clean_cup" not in st.session_state:
    st.session_state.clean_cup = 10.0
if "sweetness" not in st.session_state:
    st.session_state.sweetness = 10.0
if "overall" not in st.session_state:
    st.session_state.overall = 8.0
if "moisture" not in st.session_state:
    st.session_state.moisture = 0.11

# ---------------------------------------------------
# ENCABEZADO
# ---------------------------------------------------
st.markdown("""
<div class="titulo-principal">
☕ Sistema Inteligente de Predicción de Calidad de Café
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitulo">
Ingrese los atributos sensoriales del café y el sistema estimará la categoría de calidad automáticamente.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:
    st.header("Guía de uso")
    st.write("""
1. Ingrese los valores de cada atributo.  
2. Use números dentro del rango permitido.  
3. Presione **Predecir calidad**.  
4. Revise la categoría y las probabilidades.  
""")

    st.info("""
**Escala general**

- 0 a 10 en atributos sensoriales  
- 0 a 1 en humedad  
""")

    st.subheader("Cargar ejemplo")
    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("Ejemplo comercial", use_container_width=True):
            cargar_ejemplo("Comercial")

    with col_b:
        if st.button("Ejemplo bueno", use_container_width=True):
            cargar_ejemplo("Bueno")

    col_c, col_d = st.columns(2)

    with col_c:
        if st.button("Ejemplo muy bueno", use_container_width=True):
            cargar_ejemplo("Muy bueno")

    with col_d:
        if st.button("Ejemplo excelente", use_container_width=True):
            cargar_ejemplo("Excelente")

# ---------------------------------------------------
# INFORMACIÓN
# ---------------------------------------------------
st.markdown("""
<div class="caja-info">
<b>¿Qué significa cada dato?</b><br><br>
- <b>Aroma:</b> calidad del olor percibido.<br>
- <b>Flavor:</b> impresión general del sabor en boca.<br>
- <b>Aftertaste:</b> permanencia del sabor luego de beber.<br>
- <b>Acidity:</b> sensación de viveza o brillantez del café.<br>
- <b>Body:</b> textura o peso del café en boca.<br>
- <b>Balance:</b> armonía entre los atributos sensoriales.<br>
- <b>Uniformity:</b> consistencia entre tazas de la misma muestra.<br>
- <b>Clean Cup:</b> limpieza sensorial, sin defectos extraños.<br>
- <b>Sweetness:</b> percepción natural del dulzor.<br>
- <b>Overall:</b> evaluación global de la muestra.<br>
- <b>Moisture Percentage:</b> contenido de humedad del grano.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# FORMULARIO
# ---------------------------------------------------
st.subheader("Ingreso de datos")

col1, col2 = st.columns(2)

with col1:
    aroma = st.number_input(
        "Aroma",
        min_value=0.0, max_value=10.0, step=0.1,
        key="aroma",
        help="Evalúa la fragancia o el olor del café."
    )
    flavor = st.number_input(
        "Flavor",
        min_value=0.0, max_value=10.0, step=0.1,
        key="flavor",
        help="Evalúa el sabor general percibido."
    )
    aftertaste = st.number_input(
        "Aftertaste",
        min_value=0.0, max_value=10.0, step=0.1,
        key="aftertaste",
        help="Mide cuánto permanece el sabor luego de beber."
    )
    acidity = st.number_input(
        "Acidity",
        min_value=0.0, max_value=10.0, step=0.1,
        key="acidity",
        help="Mide la viveza o brillo del café."
    )
    body = st.number_input(
        "Body",
        min_value=0.0, max_value=10.0, step=0.1,
        key="body",
        help="Describe la textura o el peso del café en boca."
    )
    balance = st.number_input(
        "Balance",
        min_value=0.0, max_value=10.0, step=0.1,
        key="balance",
        help="Mide la armonía entre los atributos sensoriales."
    )

with col2:
    uniformity = st.number_input(
        "Uniformity",
        min_value=0.0, max_value=10.0, step=0.1,
        key="uniformity",
        help="Evalúa si las tazas de la muestra presentan consistencia."
    )
    clean_cup = st.number_input(
        "Clean Cup",
        min_value=0.0, max_value=10.0, step=0.1,
        key="clean_cup",
        help="Evalúa limpieza sensorial y ausencia de defectos."
    )
    sweetness = st.number_input(
        "Sweetness",
        min_value=0.0, max_value=10.0, step=0.1,
        key="sweetness",
        help="Mide el dulzor natural del café."
    )
    overall = st.number_input(
        "Overall",
        min_value=0.0, max_value=10.0, step=0.1,
        key="overall",
        help="Valoración general de la muestra."
    )
    moisture = st.number_input(
        "Moisture Percentage",
        min_value=0.0, max_value=1.0, step=0.01,
        key="moisture",
        help="Contenido de humedad del grano."
    )

# ---------------------------------------------------
# RESUMEN
# ---------------------------------------------------
with st.expander("Ver resumen rápido de los datos ingresados"):
    r1, r2, r3 = st.columns(3)
    with r1:
        mostrar_tarjeta_resumen("Aroma", aroma)
        mostrar_tarjeta_resumen("Flavor", flavor)
        mostrar_tarjeta_resumen("Aftertaste", aftertaste)
        mostrar_tarjeta_resumen("Acidity", acidity)
    with r2:
        mostrar_tarjeta_resumen("Body", body)
        mostrar_tarjeta_resumen("Balance", balance)
        mostrar_tarjeta_resumen("Uniformity", uniformity)
        mostrar_tarjeta_resumen("Clean Cup", clean_cup)
    with r3:
        mostrar_tarjeta_resumen("Sweetness", sweetness)
        mostrar_tarjeta_resumen("Overall", overall)
        st.metric("Moisture Percentage", f"{moisture:.2f}")

# ---------------------------------------------------
# BOTÓN DE PREDICCIÓN
# ---------------------------------------------------
if st.button("🔍 Predecir calidad", use_container_width=True):
    datos = pd.DataFrame([{
        "Aroma": aroma,
        "Flavor": flavor,
        "Aftertaste": aftertaste,
        "Acidity": acidity,
        "Body": body,
        "Balance": balance,
        "Uniformity": uniformity,
        "Clean Cup": clean_cup,
        "Sweetness": sweetness,
        "Overall": overall,
        "Moisture Percentage": moisture
    }])

    datos = datos.fillna(datos.mean(numeric_only=True))

    prediccion = modelo.predict(datos)
    categoria_predicha = prediccion[0]
    color_pred = color_categoria(categoria_predicha)

    st.markdown(
        f"""
        <div style="
            background-color:#FFF8F2;
            border-left:8px solid {color_pred};
            padding:16px;
            border-radius:12px;
            margin-top:10px;
            margin-bottom:15px;
            border:1px solid #E0CFC2;">
            <h3 style="margin:0; color:{color_pred};">Calidad predicha: {categoria_predicha}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    if hasattr(modelo, "predict_proba"):
        probabilidades = modelo.predict_proba(datos)[0]
        clases = modelo.classes_

        st.subheader("Probabilidades por categoría")

        prob_df = pd.DataFrame({
            "Categoría": clases,
            "Probabilidad": probabilidades
        }).sort_values(by="Probabilidad", ascending=False)

        for _, fila in prob_df.iterrows():
            categoria = fila["Categoría"]
            probabilidad = float(fila["Probabilidad"])
            color_barra = color_categoria(categoria)

            st.markdown(
                f"""
                <div class="bloque-categoria">
                    <div style="font-weight:600; color:{color_barra}; margin-bottom:6px;">
                        {categoria}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(probabilidad)
            st.write(f"{probabilidad:.4f}")

    st.subheader("Datos enviados al modelo")
    st.dataframe(datos, use_container_width=True)

# ---------------------------------------------------
# PIE DE PÁGINA
# ---------------------------------------------------
st.markdown("""
<div class="firma">
Desarrollado por:<br>
<b>MSc Reni Danilo Vinocunga-Pillajo Ing.</b><br>
Investigador Agregado 2
</div>
""", unsafe_allow_html=True)