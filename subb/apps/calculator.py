import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():

    a = st.number_input("Please input First Number")
    b = st.number_input("Please input Second Number")
    c = a+b
    d = a-b
    e = a*b
    f = a/b
    st.info("The result of addition is")
    st.write(c)
    st.info("The result of Subtraction is")
    st.write(d)
    st.info("The result of Multiplication is")
    st.write(e)
    st.info("The result of Division is")
    st.write(f)









