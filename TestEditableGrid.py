#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd

# Assuming you have some data in a pandas DataFrame, you can define 'df' like this:
data = {
    'command': ['ls', 'cd', 'mkdir'],
    'rating': [5, 4, 5]
}
df = pd.DataFrame(data)

# Now you can use 'df' as an argument for the st.experimental_data_editor() function:
edited_df = st.experimental_data_editor(df)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


# In[ ]:




