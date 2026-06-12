
import streamlit as st
st.title("📝 Quizzes")
q = st.radio("What is Python?",["A snake","A programming language"])
if st.button("Submit"):
    st.success("Correct!" if q=="A programming language" else "Try again")
