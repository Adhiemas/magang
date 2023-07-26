#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

mygrid = make_grid(5,5)
mygrid[0][0].write('Judul')
mygrid[1][1].write('Data 1')
mygrid[2][2].write('Data 2')
mygrid[3][3].write('Data 3')
mygrid[4][4].write('Data 4')


# In[ ]:




