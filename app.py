import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

# Titel
st.title("Open Data Dashboard")

# Daten laden
df = pd.read_csv("data.csv")

# Daten anzeigen
st.subheader("Daten")
st.write(df)

# Filter (Stadt auswählen)
city = st.selectbox("Wählen eine Stadt", df["city"].unique())

filtered_df= df[df["city"] == city]

st.subheader("Gefilterte Daten")
st.write(filtered_df)

# Bar Chart
st.subheader("Population nach Stadt")

fig, ax = plt.subplots()
df.plot(x="city", y="population", kind="bar", ax=ax)

st.pyplot(fig)

# Pie Chat
st.subheader("Population Verteilung")

fig2, ax2 = plt.subplots()
df.set_index("city")["population"].plot(kind="pie", ax=ax2)

st.pyplot(fig2)
