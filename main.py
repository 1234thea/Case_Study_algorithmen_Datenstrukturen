import streamlit as st
from tabs import users, devices, reservations, maintenance

st.title("Geräteverwaltung")
t1, t2, t3, t4 = st.tabs(["Nutzer", "Geräte", "Reservierungen", "Wartung"])
with t1:
    users.run()
with t2:
    devices.run()
with t3:
    reservations.run()
with t4:
    maintenance.run()