import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():

    a = st.number_input("Please Provide ANGle for Cosine CalCulator")
    b=math.cos(a)
    st.write(b)
    c = st.number_input("Please Provide ANGle for Sin CalCulator")
    d=math.cos(c)
    st.write(d)
    e = st.number_input("Please Provide ANGle for Tan CalCulator")
    f=math.tan(e)
    st.write(f)
 