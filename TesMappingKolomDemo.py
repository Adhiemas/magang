#!/usr/bin/env python
# coding: utf-8

# In[26]:

import streamlit as st
import mysql.connector


# In[27]:


DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = '192.168.40.11'
DATABASE_NAME = 'PBK_AOD'


# In[28]:

def create_connection():
    # Replace the connection details with your database credentials
    conn = mysql.connector.connect(
        host='192.168.40.11',
        user='wisang',
        password='Jakarta123',
        database='PBK_AOD'
    )
    return conn

conn = create_connection()


def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from [PBK_AOD].[dbo].[MappingKolom];")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")




# In[29]:


def fetch_data(conn):
    query = "SELECT * FROM [PBK_AOD].[dbo].[MappingKolom];"
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

data = fetch_data(conn)


# In[30]:


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


# In[31]:


def main():
    st.title("Update Data from SQL Database")
    display_data(data)

if __name__ == "__main__":
    main()


# In[ ]:




