
import streamlit as st

st.set_page_config(page_title="UniLearn", layout="wide")

st.title("🎓 UniLearn Platform")
st.subheader("University Learning Management System")

c1,c2,c3,c4 = st.columns(4)
c1.metric("Courses", "12")
c2.metric("Students", "250")
c3.metric("Assignments", "18")
c4.metric("Progress", "65%")

st.write("Use the sidebar to navigate through the platform.")
