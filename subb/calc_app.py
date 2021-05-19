import streamlit as st
import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd

from multiapp import MultiApp
from apps import home, calculator,tg,tg1# import your app modules here

app = MultiApp()
st.title("Simple Calculator")
st.markdown("***")

st.text("Use Drop Down menu below to navigate between Homepage and Calculator.")
st.sidebar.selectbox("NAVIGATION",[1,2,3,4,5,6,4])


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Radial Converter", tg.app)
app.add_app("Trignometry  Calculator", tg1.app)
app.add_app("Basic Calculator", calculator.app)
# The main app
app.run()