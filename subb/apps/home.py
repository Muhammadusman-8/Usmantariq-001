import streamlit as st
from PIL import Image

def app():
    st.subheader("""This is basic calculator application
    """)
    image = Image.open('Basic Calc.jpg')
    st.image(image)
    