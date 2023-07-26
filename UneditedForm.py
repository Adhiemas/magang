#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("Streamlit Form Demo")
st.subheader("Enter details below")



with st.form("form1", clear_on_submit=True):
    name = st.text_input("Enter Full Name")
    email = st.text_input("Enter Email")
    message = st.text_area("Message")
    age = st.slider("Enter Your Age", min_value = 10, max_value = 100)
    st.write(age)
    
    submit = st.form_submit_button("Submit this form")


# In[ ]:




