import streamlit as st
import pandas as pd
st.title("Hello Everyone!")
name = st.text_input("Enter your name")

age = st.slider("Select your age:", 0,100,25)
st.write(f"Your age is {age}")

options = ["Python", "Java", "C++", "Solidity"]
choice = st.selectbox("Choose your favorite language: ", options)
st.write(f"Your favorite language is {choice}")

if name:
    st.write(f"Hello {name}. You are {age} old and you selected {choice}")
data = {
    "Name": ["Yash", "Prateek", "Shreyanshi"],
    "age":  [5,21,19],
    "domain": ["Coding", "Entrepreneurip", "UPSC"]
}

df = pd.DataFrame(data)
df.to_csv("yash.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)