import streamlit as st
import pandas as pd
import pickle

with open('gold_.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Oltin narxini aniqlash")
st.write("Bu dastur sizning kiritgan ma'lumotlaringizga asoslanib oltin narxini bashorat qiladi!")

open = st.number_input("Ochilish narxi", min_value=0.0, format="%.2f")
high = st.number_input("Eng yuqori narxi", min_value=0.0, format="%.2f")
low = st.number_input("Eng past narxi", min_value=0.0, format="%.2f")

# Bashorat tugmasi
if st.button("Bashorat qilish"):
    input_data =pd.DataFrame([{
        'Open': open,
        'High': high,
        'Low': low
    }]) 
    
    prediction = model.predict(input_data)[0]
    st.success(f"Bashorat qilingan oltin narxi: ${prediction:.2f}")