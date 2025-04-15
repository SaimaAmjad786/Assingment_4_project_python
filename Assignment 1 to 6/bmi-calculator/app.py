# Project 8 : BMI Calculator

import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon=" ⚖️", layout="centered")

st.title("Project 9: BMI Calculator In Python")
# st.markdown(""" 
# ## Apna body mass index (BMI) calculate karein. Neeche apna **weight** aur **height** enter karein.
# """)
st.markdown("""
## Enter your **weight** 🏋️‍♀️ and **height** 📏 below to calculate your BMI.
""")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg) 🏋️‍♂️:", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("Height (m)📏:", min_value=1.0, format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)  # BMI formula

    st.subheader("Your BMI is:💪")
    st.markdown(f"{bmi:.2f}", unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("Underweight  😞")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal weight 🙂")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight ⚠️.")
    else:
        st.error("Obesity  🛑")
else:
    st.info("Please enter a valid weight and height  📝")







