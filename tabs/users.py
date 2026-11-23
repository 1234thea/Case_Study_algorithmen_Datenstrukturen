import streamlit as st

def run():
    st.header("Nutzer-Verwaltung")
    st.subheader("Neuen Nutzer anlegen")
    st.text_input("Name")
    st.text_input("E-Mail")
    st.button("Nutzer anlegen")