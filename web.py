import streamlit as st
import todo_functions



st.title("Todo App")

todos = todo_functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new to do...")