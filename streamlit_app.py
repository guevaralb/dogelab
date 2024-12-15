import streamlit as st

st.title("My First Streamlit App")
st.write("This is a simple Streamlit app.")

x = st.slider('Select a value', 0, 100, 50)
st.write(f'You selected {x}')
