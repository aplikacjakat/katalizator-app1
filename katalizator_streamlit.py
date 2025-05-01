# Streamlit - aplikacja lokalna
import streamlit as st

# Symulowane ceny metali w USD za gram
CENY = {
    'platyna': 32.00,
    'pallad': 45.00,
    'rod': 250.00
}

def oblicz_wartosc(platyna_g, pallad_g, rod_g):
    return round(
        platyna_g * CENY['platyna'] +
        pallad_g * CENY['pallad'] +
        rod_g * CENY['rod'], 2
    )

st.set_page_config(page_title="Wycena katalizatora", layout="centered")
st.title("Wycena katalizatora na podstawie zawartości metali")

st.markdown("Wprowadź wagę poszczególnych metali (w gramach):")

col1, col2 = st.columns(2)
with col1:
    platyna = st.number_input("Platyna (Pt)", min_value=0.0, format="%.2f")
    pallad = st.number_input("Pallad (Pd)", min_value=0.0, format="%.2f")
    rod = st.number_input("Rod (Rh)", min_value=0.0, format="%.2f")

if st.button("Oblicz wartość"):
    wartosc = oblicz_wartosc(platyna, pallad, rod)
    st.success(f"📈 Całkowita wartość katalizatora: {wartosc} USD")
