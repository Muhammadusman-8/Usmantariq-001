# import streamlit as st
# import math as mh

# st.number_input("Please Provide Value(degree) to Be Converted in Radian ")
# b=mh.radians(a)
import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():

    a = st.number_input("Please Provide Value(degree) to Be Converted in Radian")
    b=math.radians(a)
    st.write(b)
    c = st.number_input("Please Provide Value(radian) to Be Converted in Degree")
    d=math.degrees(c)
    st.write(d)
 