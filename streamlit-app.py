import streamlit as st
from rembg import remove, new_session
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="BgCut | Background Cut app with AI",
    page_icon=Image.open("favicon.png"),
    layout="wide"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

logo = Image.open('favicon.png')
st.image(logo, width=150)

st.title("BgCut - Background Cut")
st.subheader("Remova o fundo das imagens com uso de Inteligência Artificial!")
st.subheader("Arraste e solte os arquivos das imagens no local reservado no painel ao lado e veja o resultado!")
st.subheader("Para fazer download para o seu computador basta clicar na imagem com o botão direito e selecionar 'Salvar imagem como...' ")

session = new_session()

col1, col2 = st.columns(2)
images = st.sidebar.file_uploader("Carregar imagens", accept_multiple_files =True)
if images:
    for image in images:
        with Image.open(image) as img:
            with col1:
                st.header("Antes")
                st.image(img)

            with col2:
                output = remove(img, session=session)
                st.header("Depois")
                processed_img = st.image(output)

