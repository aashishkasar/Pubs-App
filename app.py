import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("WELCOME")
st.title("Pubs In United Kingdom Lets Party🍸🍹🍺")
st.write('By: :blue[Aashish]')


st.subheader(":blue[Connect with us]")

col1, col2 = st.columns(2, gap='small')
with col1:
    st.subheader("[LinkdIn](https://www.linkedin.com/in/aashishkasar/)")
with col2:
    st.subheader("[Github](https://github.com/aashishkasar)")    



st.title("🍾 🍷 🍻 🥂 🍸🍹🍺 🍔 🍟 🧀")
#Background Image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://t4.ftcdn.net/jpg/01/37/57/49/360_F_137574978_zQ5OsEYsizBPKE1FT2NWQTjdUoFpCsR1.jpg");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)