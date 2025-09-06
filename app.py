import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Algoritma Dichotomous Search
def dichotomous_search(f, a, b, epsilon=1/10, delta=1/1000):
    hasil_iterasi = []
    iterasi = 1
    while (b - a) > epsilon:
        mid = (a + b) / 2
        x1 = mid - delta
        x2 = mid + delta

        hasil_iterasi.append([
            iterasi, a, b, mid, x1, x2, f(x1), f(x2)
        ])

        if f(x1) < f(x2):
            b = x2
        elif f(x1) > f(x2):
            a = x1
        else:
            a, b = x1, x2

        iterasi += 1

    return (a + b) / 2, hasil_iterasi

# Fungsi yang akan diminimalkan
f = lambda x: (x - 2)**2

# UI Streamlit
st.title("🔎 Dichotomous Search Web App")

a = st.number_input("Masukkan batas bawah (a):", value=0.0)
b = st.number_input("Masukkan batas atas (b):", value=5.0)

if st.button("Cari Minimum"):
    hasil, tabel = dichotomous_search(f, a, b)
    st.success(f"Titik minimum kira-kira di x = {hasil:.6f}")
    st.write(f"Nilai fungsi minimum = {f(hasil):.6f}")

    # Tampilkan tabel iterasi
    df = pd.DataFrame(
        tabel,
        columns=["Iter", "a", "b", "mid", "x1", "x2", "f(x1)", "f(x2)"]
    )
    st.dataframe(df, use_container_width=True)

    # Plot grafik fungsi + titik minimum
    X = np.linspace(a, b, 200)
    Y = [f(x) for x in X]

    fig, ax = plt.subplots()
    ax.plot(X, Y, label="f(x) = (x-2)^2")
    ax.axvline(hasil, color="red", linestyle="--", label=f"Min ≈ {hasil:.3f}")
    ax.scatter([hasil], [f(hasil)], color="red", zorder=5)
    ax.set_title("Grafik Fungsi & Titik Minimum")
    ax.legend()
    st.pyplot(fig)
