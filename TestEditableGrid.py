#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd

# Assuming you have some data in a pandas DataFrame, you can define 'df' like this:

df = pd.read_csv('MS_DataSource.csv')

# Now you can use 'df' as an argument for the st.experimental_data_editor() function:
st.write("Tabel Untuk Update")
edited_df = st.data_editor(df)
st.write("Tabel Hasil Update")
edited_df.update(edited_df, overwrite=True)
st.write(edited_df)




# In[ ]:




