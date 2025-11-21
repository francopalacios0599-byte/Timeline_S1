import streamlit as st

st.set_page_config(page_title="Timeline con Slider", layout="centered")

st.title("Timeline con Slider desde GitHub")

# Lista de imágenes (raw URLs desde GitHub)
# Reemplaza 'usuario', 'repo' y 'branch'
image_paths = [
    "https://raw.githubusercontent.com/usuario/repo/branch/timeline_images/img1.jpg",
    "https://raw.githubusercontent.com/usuario/repo/branch/timeline_images/img2.jpg",
    "https://raw.githubusercontent.com/usuario/repo/branch/timeline_images/img3.jpg",
    "https://raw.githubusercontent.com/usuario/repo/branch/timeline_images/img4.jpg",
    "https://raw.githubusercontent.com/usuario/repo/branch/timeline_images/img5.jpg"
]

# Slider de 1 a 5
index = st.slider("Selecciona un punto del timeline", 1, 5, 1)

# Mostrar imagen correspondiente
st.image(image_paths[index - 1], use_column_width=True)
