# katalizator_app.py — Profesjonalna aplikacja do wyceny katalizatorów
import streamlit as st
import pandas as pd
from io import BytesIO

# Przykładowe ceny metali w zł/g (docelowo do podpięcia z API)
CENY_METALI = {
    'PT': 120.0,
    'PD': 180.0,
    'RH': 1400.0
}

# Obliczanie wartości
def licz_wartosc(pt, pd, rh):
    return round(pt * CENY_METALI['PT'] + pd * CENY_METALI['PD'] + rh * CENY_METALI['RH'], 2)

st.set_page_config(page_title="Kalkulator Katalizatorów PRO", layout="centered")
st.title("📦 Profesjonalna wycena katalizatorów")
st.markdown("Wgraj plik Excel z kolumnami NUMER, WAGA, PT, PD, RH. Aplikacja przeliczy wartość na podstawie aktualnych cen.")

uploaded_file = st.file_uploader("📁 Wgraj plik Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        required_cols = ['NUMER', 'WAGA', 'PT', 'PD', 'RH']
        if not all(col in df.columns for col in required_cols):
            st.error(f"Brakuje wymaganych kolumn: {required_cols}")
        else:
            df['WARTOŚĆ zł'] = df.apply(lambda row: licz_wartosc(row['PT'], row['PD'], row['RH']), axis=1)
            st.success("✅ Przetworzono dane.")
            st.dataframe(df[['NUMER', 'WAGA', 'PT', 'PD', 'RH', 'WARTOŚĆ zł']])

            def convert_df(df):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False)
                return output.getvalue()

            st.download_button(
                label="📥 Pobierz wynik jako Excel",
                data=convert_df(df),
                file_name="wycena_katalizatorow.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    except Exception as e:
        st.error(f"Błąd: {e}")
else:
    st.info("📄 Wgraj plik, aby rozpocząć.")
