import streamlit as st

name= st.text_input("Enter your name: ")
SurName= st.text_input("Enter your surname: ")
adr = st.text_area("Enter your address: ")
classdata= st.selectbox("Enter your class year:",(1,2,3,4))

button= st.button("Done")
if button:
    st.markdown(f"""
                Name : {name}\n
                Surname : {SurName}\n
                Address: {adr}\n
                Class : {classdata}""")