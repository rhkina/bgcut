import streamlit as st
from rembg import remove
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

st.title("BgCut - Background Cut using AI")
st.subheader("Remove background from images using AI!")
st.subheader("Just drag and drop image files and see the result! Multiple files allowed!")
st.subheader("Right click the resulting images and select 'Save as...' to download to your computer")

st.subheader(":mailbox: Hi! Do you want to receive our news occasionally? No spams, we hate spams as you do!")

contact_form = """
    <form action="https://formsubmit.co/rhkina@gmail.com" method="POST">
        <input type="hidden" name="_captha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

col1, col2 = st.columns(2)
images = st.sidebar.file_uploader("Carregar imagens", accept_multiple_files =True)
if images:
    for image in images:
        with Image.open(image) as img:
            with col1:
                st.header("Before")
                st.image(img)

            with col2:
                output = remove(img)
                st.header("After")
                processed_img = st.image(output)

