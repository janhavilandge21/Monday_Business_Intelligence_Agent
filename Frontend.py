import streamlit as st
from insights import generate_insight

st.title("📊 AI Business Intelligence Agent")

question = st.text_input("Ask your business question")

if st.button("Get Insight"):
    if question:
        result = generate_insight(question)

        st.success(result)
