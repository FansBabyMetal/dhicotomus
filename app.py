import streamlit as st
import math

def dichotomous_search(f, a, b, epsilon=1/10, delta=1/1000):
    """
    f       : fungsi yang akan diminimalkan
    a, b    : batas interval pencarian
    epsilon : toleransi error
    delta   : jarak kecil dari titik tengah
    """
    hasil_iterasi = []
    iterasi = 1

    while (b - a) > epsilon:
        mid = (a + b) / 2
        x1 = mid - delta/2
        x2 = mid + delta/2

        if f(x1) < f(x2) - 1e-12:
            b = x2   # minimum ada di kiri
        elif f(x1) > f(x2) + 1e-12:
            a = x1   # minimum ada di kanan
        else:
            a = x1
            b = x2

        hasil_iterasi.append({
            "Iter": iterasi,
            "a": a,
            "b": b,
            "mid": mid,
            "x1": x1,
            "x2": x2,
            "f(x1)": f(x1),
            "f(x2)": f(x2)
        })

        iterasi += 1

    return (a + b) / 2, hasil_iterasi


# ==============================
# Streamlit App
# ==============================
st.title("🔎 Dichotomous Search - Pencarian Minimum")

st.write("Aplikasi ini menggunakan **Dichotomous Search** untuk mencari titik minimum dari fungsi yang diberikan.")

# Input dari user
f_input = st.text_input("Masukkan fungsi f(x)", "(x - 2)**2")
a = st.number_input("Masukkan batas bawah (a)", value=0.0)
b = st.number_input("Masukkan batas atas (b)", value=4.0)
epsilon = st.number_input("Toleransi error (epsilon)", value=0.1)
delta = st.number_input("Nilai delta", value=0.001)

if st.button("Jalankan Pencarian"):
    try:
        f = lambda x: eval(f_input, {"x": x, "math": math})

        hasil, iterasi_data = dichotomous_search(f, a, b, epsilon, delta)

        st.success(f"Titik minimum kira-kira di **x = {hasil:.6f}**")
        st.success(f"Nilai fungsi minimum = {f(hasil):.6f}")

        st.subheader("📊 Tabel Iterasi")
        st.dataframe(iterasi_data)

    except Exception as e:
        st.error(f"Terjadi error: {e}")
