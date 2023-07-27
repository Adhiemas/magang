#!/usr/bin/env python
# coding: utf-8

# In[22]:


import streamlit as st
import pypyodbc as odbc


# In[16]:


DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = '192.168.40.11'
DATABASE_NAME = 'PBK_AOD'


# In[18]:


connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    uid=wisang;
    pwd=Jakarta123;
"""

conn = odbc.connect(connection_string)
print(conn)


# In[19]:


def fetch_data(conn):
    query = "SELECT * FROM [PBK_AOD].[dbo].[MappingKolom];"
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

data = fetch_data(conn)


# In[20]:


def display_data(data):
    for row in data:
        st.write(row)

    # You can add user input elements (e.g., text inputs, select boxes) to allow updates
    # For example, let's say you want to update a 'status' column in your_table
    selected_row_index = st.number_input("Enter the row number to update", min_value=1, max_value=len(data))

    if selected_row_index:
        selected_row = data[selected_row_index - 1]
        new_status = st.text_input("Enter the new status", selected_row['status'])
        if st.button("Update"):
            update_status(conn, selected_row['id'], new_status)
            st.success("Update successful!")

def update_status(conn, row_id, new_status):
    query = "UPDATE your_table SET status = %s WHERE id = %s;"
    cursor = conn.cursor()
    cursor.execute(query, (new_status, row_id))
    conn.commit()
    cursor.close()


# In[23]:


def main():
    st.title("Update Data from SQL Database")
    display_data(data)

if __name__ == "__main__":
    main()


# In[ ]:




