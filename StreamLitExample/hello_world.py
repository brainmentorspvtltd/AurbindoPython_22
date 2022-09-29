import streamlit as st

st.write("Hello How are you...???")
st.write("Simple Streamlit Example...")

val = st.slider("val_1")
st.write(val, "squared is :",val * val)

val = st.slider("val_2")
st.write(val, "cube is :",val ** 3)

