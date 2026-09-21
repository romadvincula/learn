# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(f":apple: Uncle Yer's Fruit Details :apple:")
st.write(
  """Enter fruit name and root depth code below.
  """
)

# Get the current credentials
session = get_active_session()

# capture entered values
fn = st.text_input('Fruit Name:')
rdc = st.selectbox('Root Depth:', ('S','M','D'))

# submit the values
if st.button('Submit'):
    # st.write('Fruit Name entered is ' + fn)
    # st.write(f'Root Depth Code chosen is {rdc}')

    sql_insert = 'insert into garden_plants.fruits.fruit_details select \''+fn+'\', \''+rdc+'\''
    # st.write(sql_insert)
    result = session.sql(sql_insert)
    st.write(result)
