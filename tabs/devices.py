import streamlit as st

def run():
    st.header("Geräte-Verwaltung")
    st.selectbox("Gerät auswählen", ["Neues anlegen", "Vorhandenes berarbeiten"])
    st.subheader("Gerätedaten eingeben")
    st.number_input("Inventarnummer (ID)", step=1)
    st.text_input("Names des Gerätes")
    st.button("Bestätigen")